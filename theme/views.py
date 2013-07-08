from django.views.generic import FormView, UpdateView
from django.core.urlresolvers import reverse_lazy as reverse

from forms import ThemeForm

from models import Theme

class ThemeFormView(FormView):
    form_class = ThemeForm
    template_name = 'theme/theme_edit.html'
    success_url = reverse('dashboard') # Sample success url.

    def form_valid(self, form):
        name = form.cleaned_data['name']
        theme_color = form.cleaned_data['theme_color']
        background_image = form.cleaned_data['background_image']
        theme = Theme(name=name, theme_color=theme_color, background_image=background_image)
        theme.save()

class ThemeUpdateView(UpdateView):
    model = Theme
    form_class = ThemeForm
    template_name = 'theme/theme_edit.html'
    success_url = reverse('dashboard')