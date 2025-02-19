from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Homepage route for parking app
]