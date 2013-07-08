from django.core.management.base import NoArgsCommand, CommandError
from django.template.loader import render_to_string
from django.core.files.base import ContentFile

from ...models import Theme
from ...tasks import compile_less

class Command(NoArgsCommand):
    help = 'Generate the theme files from model instance.'

    def handle_noargs(self, **options):
        try:
            all_themes = Theme.objects.all()
        except Theme.DoesNotExist:
            raise CommandError('There is not any theme.')
        for theme in all_themes:
            compile_less(theme, theme.get_less_content())
            self.stdout.write('%s themes generated.' % all_themes.count())