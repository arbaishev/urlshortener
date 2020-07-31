from django.conf import settings
from random import choice as randchoice
import string

SHORTCODE_SIZE = getattr(settings, "SHORTCODE_SIZE", 6)


def code_generator(size=6, chars=string.ascii_letters + string.digits):
    return ''.join(randchoice(chars) for _ in range(size))


def create_shortcode(instance, size=SHORTCODE_SIZE):
    new_code = code_generator(size=size)
    qs_exists = instance.__class__.objects.filter(shortcode=new_code).exists()
    if qs_exists:
        return create_shortcode(size=size)
    return new_code
