from django import forms

from .validators import validate_url


class URLForm(forms.Form):
    url = forms.CharField(label="Long URL:",
                          validators=[validate_url],
                          widget=forms.TextInput(
                              attrs={
                                  "placeholder": "Long URL"
                              }
                          )
                          )
    custom_shortcode = forms.SlugField(label="Custom shortcode (optional):", required=False)
