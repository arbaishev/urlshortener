from django.urls import path

from . import views

urlpatterns = [
    path('api/', views.URLListView.as_view()),
    path('api/<shortcode>', views.URLStats.as_view()),
    path('api/short/', views.URLShortener.as_view()),
]

app_name = 'api'
