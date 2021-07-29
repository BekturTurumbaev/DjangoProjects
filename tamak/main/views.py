from django.shortcuts import render, redirect, reverse
from django.views.generic import View
from .forms import RegistrationForm, CommentForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib import messages
from django.views.generic import View, CreateView, ListView, DetailView, DeleteView, UpdateView
from .models import Feedback, Comment

class FeedbacksCreateView(LoginRequiredMixin, CreateView):
    template_name = 'main/feedback_create.html'
    model = Feedback
    fields = ['body']

    def get_success_url(self):
        return reverse('main:feedback-list')

    def form_valid(self, form):
        form.save(commit=False)
        form.instance.user = self.request.user
        form.save()
        return super(FeedbacksCreateView, self).form_valid(form)

class FeedbacksListVeiw(ListView):
    template_name = 'main/feedback_list.html'
    model = Feedback
    ordering = '-date'

class FeedbackDetailView(View):

    def get(self, request, pk):
        form = CommentForm()

        feed = Feedback.objects.get(id=pk)
        comments = Comment.objects.filter(feedback_id=pk)

        return render(request, template_name="main/feedback_details.html", context={"form": form, "object": feed, "comments": comments})

    # def get_context_data(self, **kwargs):
    #     feedback = self.get_object()
    #     form = CommentForm() # Мы сами создали это форму в forms.py
    #     kwargs["form"] = form
    #     kwargs["comments"] = Comment.objects.filter(
    #         feedback_id = feedback.pk
    #     )
    #     return super().get_context_data(**kwargs)

    def post(self, request, pk): # Здесь pk аргумент это та самая цифра из URL в браузере, она подставляется автоматически
        form = CommentForm(request.POST)

        form.save(commit=False)
        form.instance.user = request.user # Тут мы добавляем автора
        feedback = Feedback.objects.get(id=pk)
        form.instance.feedback_id = pk # Тут мы добавляем отзыв к которому будет привязан комментарий

        comments = Comment.objects.filter(feedback_id=pk)

        if form.is_valid():
            form.save()

        form = CommentForm()
        return render(
            request,
            template_name="main/feedback_details.html",
            context={"form": form, "object": feedback, "comments": comments},
        )

class FeedbackUpdateView(UserPassesTestMixin, UpdateView):
    template_name = 'main/feedback_update.html'
    model = Feedback
    fields = ['body']

    def get_success_url(self) -> str:
        return reverse('main:feedback-list')

    def test_func(self):
        movie = self.get_object()
        if movie.user == self.request.user:
            return True
        return False


class FeedbackDeleteView(UserPassesTestMixin, DeleteView):
    template_name = 'main/feedback_delete.html'
    model = Feedback

    def get_success_url(self) -> str:
        return reverse('main:feedback-list')

    def test_func(self):
        movie = self.get_object()
        if movie.user == self.request.user:
            return True
        return False

class MainView(View):
    def get(self, request):
        return render(request, template_name="main/main.html")
        

class AboutView(LoginRequiredMixin,View):
    def get(self, request): 
        return render(request, template_name="main/about.html")
        
class RegistrationView(View):
    def get(self, request):
        custom_user_form=RegistrationForm()
        return render(request, template_name="main/registration.html",context={'form':custom_user_form})
    def post(self,request):
        custom_user_form=RegistrationForm(request.POST)

        if custom_user_form.is_valid():
            custom_user_form.save()
            messages.success(request,'Вы успешно зарегестировались!')
            return redirect('login')

        errors = []
        for key in custom_user_form.errors:
            errors.append(custom_user_form.errors.get(key))
        custom_user_form=RegistrationForm()
        return render(request, template_name="main/registration.html",context={'form':custom_user_form, 'errors': errors})

# from django.shortcuts import render, redirect, reverse
# from django.views.generic import View
# from .forms import RegistrationForm, CommentForm
# from django.contrib.auth.mixins import LoginRequiredMixin
# from django.contrib import messages
# from django.views.generic import View, CreateView, ListView, DetailView
# from .models import Feedback, Comment

# class FeedbacksCreateView(LoginRequiredMixin, CreateView):
#     template_name = 'main/feedback_create.html'
#     model = Feedback
#     fields = ['body']

#     def get_success_url(self):
#         return reverse('main:feedback-list')

#     def form_valid(self, form):
#         form.save(commit=False)
#         form.instance.user = self.request.user
#         form.save()
#         return super(FeedbacksCreateView, self).form_valid(form)

# class FeedbacksListVeiw(ListView):
#     template_name = 'main/feedback_list.html'
#     model = Feedback
#     ordering = '-date'

# class FeedbackDetailView(DetailView):
#     model = Feedback
#     template_name = "main/feedback_details.html"
    

#     def get_context_data(self, **kwargs):
#         feedback = self.get_object()
#         form = CommentForm() # Мы сами создали это форму в forms.py
#         kwargs["form"] = form
#         kwargs["comments"] = Comment.objects.filter(
#             feedback_id = feedback.pk
#         )
#         return super().get_context_data(**kwargs)

#     def post(self, request, pk): # Здесь pk аргумент это та самая цифра из URL в браузере, она подставляется автоматически
#         form = CommentForm(request.POST)

#         form.save(commit=False)
#         form.instance.user = request.user # Тут мы добавляем автора
#         feedback = Feedback.objects.get(id=pk)
#         form.instance.feedback_id = pk # Тут мы добавляем отзыв к которому будет привязан комментарий

#         comments = Comment.objects.filter(feedback_id=pk)

#         if form.is_valid():
#             form.save()

#         form = CommentForm()
#         return render(
#             request,
#             template_name="main/feedback_details.html",
#             context={"form": form, "object": feedback, "comments": comments},
#         )


# class MainView(View):
#     def get(self, request):
#         return render(request, template_name="main/main.html")
        

# class AboutView(LoginRequiredMixin,View):
#     def get(self, request): 
#         return render(request, template_name="main/about.html")
        
# class RegistrationView(View):
#     def get(self, request):
#         custom_user_form=RegistrationForm()
#         return render(request, template_name="main/registration.html",context={'form':custom_user_form})
#     def post(self,request):
#         custom_user_form=RegistrationForm(request.POST)

#         if custom_user_form.is_valid():
#             custom_user_form.save()
#             messages.success(request,'Вы успешно зарегестировались!')
#             return redirect('login')

#         errors = []
#         for key in custom_user_form.errors:
#             errors.append(custom_user_form.errors.get(key))
#         custom_user_form=RegistrationForm()
#         return render(request, template_name="main/registration.html",context={'form':custom_user_form, 'errors': errors})