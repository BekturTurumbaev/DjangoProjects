from django.urls import path
from .views import HomeView, AboutView, NewsView, ServicesView, MainView
from .forms import LoginForm
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('', MainView.as_view(), name='main_page'),
    path('login/', LoginView.as_view(template_name=',main/home.html', authentication_form=LoginForm), name='login_view'),
    path('home/', HomeView.as_view(), name='home_view'),
    path('about/', AboutView.as_view(), name='about_view'),
    path('news/', NewsView.as_view(), name='news_view'),
    path('services/', ServicesView.as_view(), name='servis_view'),
    path('logout/', LogoutView.as_view(template_name='main/logout.html'), name='logout_view'),
]
