from . import views
from django.urls import path


urlpatterns = [
    path('', template_name='main/wrapper'),
]