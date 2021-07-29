
from django.shortcuts import render
from django.views.generic import View, ListView, DetailView
from .models import PrimaryMeal, GeneralMeal, Wine

class PrimaryMealsView(ListView):
    template_name = 'menu/primary_meals.html'
    model = PrimaryMeal

    def get_context_data(self, **kwargs):
        
        kwargs["breakfast"] = GeneralMeal.objects.filter(types='1')#.filter(srok__range=[start, end])
        kwargs["lunch"] = GeneralMeal.objects.filter(types='2')#.filter(srok__range=[start, end])
        kwargs["dinner"] = GeneralMeal.objects.filter(types='3')#.filter(srok__range=[start, end])

        return super().get_context_data(**kwargs)


class PrimaryMealsDetailView(DetailView):
    template_name = 'menu/primary_details.html'
    model = PrimaryMeal

class WinesView(ListView):
    template_name = 'menu/wines.html'
    model = Wine

    def get_context_data(self, **kwargs):
        
        kwargs["primary_wine"] = Wine.objects.filter(types='1')#.filter(srok__range=[start, end])
        kwargs["wines"] = Wine.objects.filter(types='2')#.filter(srok__range=[start, end])

        return super().get_context_data(**kwargs)


class WinesDetailView(DetailView):
    template_name = 'menu/wine_details.html'
    model = Wine



    