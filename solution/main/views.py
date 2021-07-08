from django.shortcuts import render, redirect
from django.views.generic import View
from .forms import CustomUserForm, LoginForm
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.mail import send_mail, BadHeaderError
from .models import (
    AboutViewSubjects1, AboutViewSubjects2, AboutViewSubjects3, AboutViewSubjects4, AboutViewSubjects5,
    HomeViewSubjects1,
    NewsViewSubjects1, NewsViewSubjects2, NewsViewSubjects3, 
    ServicesViewSubjects1, ServicesViewSubjects2, ServicesViewSubjects3,
    )

class MainView(View):
    def get(self, request):
        login_forms = LoginForm()
        custom_user_form = CustomUserForm()
        return render(request, template_name='main/home.html', context={'reg_form': custom_user_form, 'login_form': login_forms})

    def post(self, request):
        if request.POST.get('submit') == 'signup':
            custom_user_form = CustomUserForm(request.POST)

            if custom_user_form.is_valid():
                custom_user_form.save()

                messages.success(request, 'Registration success')
                return render(request, template_name='main/home.html')
            
            error = '\n'.join([msg[0] for msg in tuple(custom_user_form.errors.values())])
            messages.warning(request, error)
            custom_user_form = CustomUserForm()
            return render(request, template_name='main/home.html', context={'reg_form': custom_user_form})

class HomeView(LoginRequiredMixin, View):
    def get(self, request):
        tema = HomeViewSubjects1.objects.all()
        return render(request, template_name="main/home.html", context={'topics': tema})

class AboutView(LoginRequiredMixin, View): 
    def get(self, request):
        about_start = AboutViewSubjects1.objects.all()
        text = AboutViewSubjects2.objects.all()
        worker = AboutViewSubjects3.objects.all()
        more = AboutViewSubjects4.objects.all()
        advert_logo = AboutViewSubjects5.objects.all()
        return render(request, template_name="main/about.html", context={'data': about_start, 'texts': text, 'workers': worker, 'mores': more, 'images': advert_logo})

    def post(self, request):
        subject = f"Message from {request.user.first_name} {request.user.last_name}"
        email = request.POST.get("email", "")
        message = request.POST.get("message", "")

        try:
            send_mail(subject, message, email)
            messages.success(request, 'Message has been send successfully!')
        except BadHeaderError as e:
            messages.warning(request, f"Message can't be send because {e}")

        return redirect('about_view')

class NewsView(LoginRequiredMixin, View):
    def get(self, request):
        text = NewsViewSubjects1.objects.all()
        pictures = NewsViewSubjects2.objects.all()
        data = NewsViewSubjects3.objects.all()
        return render(request, template_name="main/news.html", context={"pictures": pictures, "texts": text, "data": data})

class ServicesView(LoginRequiredMixin, View):
    def get(self, request):
        text = ServicesViewSubjects1.objects.all()
        data_1 = ServicesViewSubjects2.objects.all()
        data_2 = ServicesViewSubjects3.objects.all()
        return render(request, template_name="main/services.html", context={"texts": text, "data_1": data_1, "data_2": data_2})
