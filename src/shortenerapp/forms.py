from django import forms

from .validators import validate_url


class URLForm(forms.Form):
    url = forms.CharField(label='',
                          validators=[validate_url],
                          widget=forms.TextInput(
                              attrs={
                                  "placeholder": "Long URL"
                              }
                          )
                          )