from django.urls import path
from .views import TeamView, DetailTeamView

app_name = 'teams'
urlpatterns = [
    path('teams/', TeamView.as_view(), name='teams'),
    path('teams/details/<int:pk>/', DetailTeamView.as_view(), name='teams-details'),
]
# {% url 'teams:teams-details' teams.pk %}