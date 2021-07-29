from typing import List
from django.shortcuts import render, reverse
from django.views.generic import View, ListView, CreateView, DetailView
from django.views.generic.edit import FormView
from .forms import CreateTeamsForm
from .models import Teams

class TeamView(FormView):
    template_name = 'teams/team_list.html'
    form_class = CreateTeamsForm
    fields = ['user', 'position', 'education', 'experience', 'companies']

    def get_success_url(self):
        return reverse('main:main')

    # def get(self, request, pk):
    #     teams = Teams.objects.all()
    #     return render(
    #         request,
    #         template_name="teams/team_list.html",
    #         context={"team": teams},
    #     )

    def get_context_data(self, **kwargs):
        kwargs["teams"] = Teams.objects.all()

        return super().get_context_data(**kwargs)

class DetailTeamView(DetailView):
    template_name = 'teams/teams_details.html'
    model = Teams