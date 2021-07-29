from django.urls import path
from .views import MainView, AboutView, FeedbacksCreateView, FeedbacksListVeiw, FeedbackDetailView, FeedbackUpdateView, FeedbackDeleteView

app_name = 'main'
urlpatterns = [
    path('', MainView.as_view(), name='main'),
    path('about/', AboutView.as_view(), name='about'),
    path('feedback/create/', FeedbacksCreateView.as_view(), name='feedback-create'),
    path('feedback/all/', FeedbacksListVeiw.as_view(), name='feedback-list'),
    path('feedback/details/<int:pk>/', FeedbackDetailView.as_view(), name='feedback-details'),
    path('feedback/update/<int:pk>/', FeedbackUpdateView.as_view(), name='feedback-update'),
    path('feedback/delete/<int:pk>/', FeedbackDeleteView.as_view(), name='feedback-delete'),
]
