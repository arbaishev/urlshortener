from django.core.exceptions import ValidationError
from django.core.validators import URLValidator


def validate_url(url):
    input_url = url
    url_validator = URLValidator()
    if "http" not in input_url:
        input_url = "http://" + input_url
    try:
        url_validator(input_url)
    except:
        raise ValidationError("Invalid URL")
    return input_url
