from django.urls import path
from .views import ReservationsView, CreateReservationsView

app_name = 'reservation'
urlpatterns = [
    path('reservation/', ReservationsView.as_view(), name='reservation'),
    path('create-reservation/', CreateReservationsView.as_view(), name='create_reservation'),
]
