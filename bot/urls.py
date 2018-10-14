from django.urls import path
from .views import MainView

urlpatterns = [
    path('webhook/', MainView.as_view()),
]
