from django.urls import path
from .views import HomeView, AboutView, NewsView, ServicesView

urlpatterns = [
    path("home/", HomeView.as_view(), name="home_view"),
    path("about/", AboutView.as_view(), name="about_view"),
    path("news", NewsView.as_view(), name="news_view"),
    path("services/", ServicesView.as_view(), name="servis_view"),
]
