from django.urls import path
from .views import MainView


app_name = 'bot'
urlpatterns = [
    path('webhook/', MainView.as_view()),
]
