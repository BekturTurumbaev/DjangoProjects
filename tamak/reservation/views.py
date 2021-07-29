from django.shortcuts import render, reverse
from django.views.generic import View, CreateView, ListView
from .models import CreateReservationModel
from .forms import CreateReservationsForm
from django.views.generic.edit import FormView
from django.contrib.auth.mixins import LoginRequiredMixin

class ReservationsView(LoginRequiredMixin, View):
    def get(self, request):
        reserv = CreateReservationModel.objects.filter(client_id = request.user.id)

        return render(request, template_name="reservation/reservations_list.html", context={"createreservationmodel_list": reserv})


class CreateReservationsView(LoginRequiredMixin, FormView):
    template_name = 'reservation/reservations_create.html'
    form_class = CreateReservationsForm
    
    def get_success_url(self):
        return reverse('main:main')

    def form_valid(self, form):
        form.save(commit=False)
        form.instance.client = self.request.user
        form.save()
        return super(CreateReservationsView, self).form_valid(form)


