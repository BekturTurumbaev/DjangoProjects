from django.shortcuts import render
from django.views.generic import View

class HomeView(View):
    def get(self, request):
        return render(request, template_name="main/home.html")

class AboutView(View):
    def get(self, request):
        return render(request, template_name="main/about.html")

class NewsView(View):
    def get(self, request):
        return render(request, template_name="main/news.html")

class ServicesView(View):
    def get(self, request):
        return render(request, template_name="main/services.html")