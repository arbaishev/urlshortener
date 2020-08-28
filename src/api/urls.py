from django.urls import path, re_path

from . import views

urlpatterns = [
    path('api', views.URLListView.as_view()),
    path('api/stats/<slug:shortcode>', views.URLStats.as_view()),
    path('api/short', views.URLShortener.as_view()),
    re_path(r'^api/.*$', views.error404)
]

app_name = 'api'
