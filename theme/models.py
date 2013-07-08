from django.db import models
from django.conf import settings
from django.dispatch import receiver
from django.utils.text import slugify
from django.db.models import signals
from django.template.loader import render_to_string
from django.core.files.base import ContentFile

from tasks import compile_less

class Theme(models.Model):
    def get_upload_path(self, filename):
        """
        Gets the upload path for files
        """
        filename = filename.split('.')
        extension = filename.pop()
        name = ''.join(filename)
        return "themes/%s.%s" % (slugify(unicode(name)), extension)

    name = models.CharField(max_length=250)
    theme_color = models.CharField(max_length=7)
    background_image = models.ImageField(upload_to=get_upload_path, blank=True)
    less_file = models.FileField(upload_to=get_upload_path, blank=True)
    compiled_css_file = models.FileField(upload_to=get_upload_path, blank=True)

    def __unicode__(self):
        return self.name

    def get_less_content(self):
        less_content = render_to_string('theme/theme.less', {'instance' : self})
        self.less_file.save('theme.less', ContentFile(less_content), save=False)
        return less_content

@receiver(signals.post_save, sender=Theme)
def generate_less_file(sender, instance, *args, **kwargs):
    if not getattr(instance, '_do_not_compile', None):
        compile_less.delay(instance, instance.get_less_content())