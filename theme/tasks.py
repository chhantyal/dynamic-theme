import celery
import subprocess

from django.core.files.base import ContentFile
from django.template.loader import render_to_string

@celery.task
def compile_less(instance, less_content):
    p = subprocess.Popen(['lessc', '-x', '-'], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    output = p.communicate(less_content)
    css_content = output[0]
    instance._do_not_compile = True
    instance.compiled_css_file.save('style.css', ContentFile(css_content))
