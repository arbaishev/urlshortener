from django.urls import path

from . import views

urlpatterns = [
    path('<shortcode>', views.URLRedirect.as_view()),
    path('', views.HomeView.as_view(), name='index'),
]

app_name = 'shortenerapp'
