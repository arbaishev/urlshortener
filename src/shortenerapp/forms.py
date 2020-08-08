from django import forms

from .validators import validate_url


class URLForm(forms.Form):
    url = forms.CharField(
        label="",
        validators=[validate_url],
        widget=forms.TextInput(
            attrs={
                "placeholder": "Input long URL here",
            }
        )
    )

    custom_shortcode = forms.SlugField(
        label="",
        max_length=6,
        required=False,
        widget=forms.TextInput(
            attrs={
                "placeholder": "Custom alias (optional)",
            }
        )
    )


