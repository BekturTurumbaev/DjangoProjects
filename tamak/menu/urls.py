from django.urls import path
from .views import PrimaryMealsView, WinesView, PrimaryMealsDetailView, WinesDetailView

app_name = 'menu'
urlpatterns = [
    path('meals/', PrimaryMealsView.as_view(), name='meals'),
    path('meals-detail/<int:pk>/', PrimaryMealsDetailView.as_view(), name='meals-detail'),
    path('wines/', WinesView.as_view(), name='wines'),
    path('wines/details/<int:pk>/', WinesDetailView.as_view(), name='wines-details'),
]
