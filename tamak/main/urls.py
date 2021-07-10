from . import views
from django.urls import path
from .views import MainView, AboutView, FeedbacksView

app_name = 'main'
urlpatterns = [
    path('', MainView.as_view(), name='main'),
    path('about/', AboutView.as_view(), name='about'),
    path('feedbacks/', FeedbacksView.as_view(), name='feedbacks'),
]
