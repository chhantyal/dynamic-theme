from django import forms

from .models import Theme

class ThemeForm(forms.ModelForm):
    class Meta:
        model = Theme
        fields = ['name', 'theme_color', 'background_image']
        widgets = {
            'theme_color': forms.TextInput(attrs={'class': 'colorpicker'}),
        }