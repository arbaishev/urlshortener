from django.db import models
from .utils import create_shortcode
from .validators import validate_url


class URL(models.Model):
    url = models.URLField(max_length=220, validators=[validate_url])
    shortcode = models.SlugField(max_length=6, unique=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    count = models.IntegerField(default=0)

    def save(self, *args, **kwargs):
        if self.shortcode is None or self.shortcode == "":
            self.shortcode = create_shortcode(self)
        if not "http" in self.url:
            self.url = "http://" + self.url
        super(URL, self).save(*args, **kwargs)

    def clicked(self):
        self.count += 1
        self.save()

    def __str__(self):
        return str(self.url)

    def __unicode__(self):
        return str(self.url)
