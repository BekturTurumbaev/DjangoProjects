from django.contrib.messages.api import error
from django.shortcuts import redirect, render
from django.views.generic import View
from .forms import CustomUserForm
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import auth 

class MainView(View):
    def get(self, request):
        return render(request, template_name='main/main.html')

class AboutView(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, template_name='main/about.html')

class FeedbacksView(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, template_name='main/feedbacks.html')

class RegistrationView(LoginRequiredMixin, View):
    def get(self, request):
        custom_user_form = CustomUserForm()
        return render(request, template_name='main/registration.html', context={'reg_form': custom_user_form})

    def post(self, request):
        custom_user_form = CustomUserForm(request.POST)

        if custom_user_form.is_valid():
            custom_user_form.save()

            messages.success(request, 'Registration success')
            return redirect('login')
    
        errors = []
        for key in custom_user_form.errors:
            errors.append(custom_user_form.errors.get(key))
        
        custom_user_form = CustomUserForm()
        return render(request, template_name='main/registration.html', context={'reg_form': custom_user_form, 'errors': errors})
