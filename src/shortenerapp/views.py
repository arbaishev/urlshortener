from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View

from .forms import URLForm
from .models import URL


class URLRedirect(View):
    def get(self, request, shortcode=None, *args, **kwargs):
        url = get_object_or_404(URL, shortcode=shortcode)
        url.clicked()
        return redirect(f"{url.url}")


class HomeView(View):
    def get(self, request, *args, **kwargs):
        the_form = URLForm()
        context = {
            "title": "Url Shortener",
            "form": the_form,
        }
        return render(request, "shortenerapp/index.html", context)

    def post(self, request, *args, **kwargs):
        form = URLForm(request.POST)
        context = {
            "title": "Url Shortener",
            "form": form,
        }
        template = "shortenerapp/index.html"

        if form.is_valid():
            new_url = form.cleaned_data.get("url")

            if not form.cleaned_data.get("custom_shortcode"):
                obj, created = URL.objects.filter(url=new_url, custom=False).get_or_create(url=new_url)
            else:
                new_shortcode = form.cleaned_data.get("custom_shortcode")

                if not URL.objects.filter(shortcode=new_shortcode).exists():
                    obj, created = URL.objects.get_or_create(url=new_url, shortcode=new_shortcode, custom=True)
                else:
                    messages.error(request, "Shortcode already exists")
                    return render(request, template, {"form": form})

            context["object"] = obj
            context["created"] = created
            context["shorturl"] = request.build_absolute_uri() + obj.shortcode

        return render(request, template, context)
