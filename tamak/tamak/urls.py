from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from main.views import RegistrationView
from django.conf.urls.static import static
from main.views import RegistrationView
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', LoginView.as_view(template_name = 'main/login.html'), name='login'),
    path('registration/', RegistrationView.as_view(), name='registration'),
    path('logout/', LogoutView.as_view(template_name = 'main/logout.html'), name='logout'),
    path('', include('main.urls')),
    path('menu/', include('menu.urls')),
    path('reserv/', include('reservation.urls')),
    path('teams/', include('teams.urls')),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
