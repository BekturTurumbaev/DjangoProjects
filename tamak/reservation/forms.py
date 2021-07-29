from django import forms
from django.forms import widgets
from .models import CreateReservationModel

class CreateReservationsForm(forms.ModelForm):
    class Meta:
        model = CreateReservationModel
        exclude = ['client']

        widgets = {
        "phone_number": forms.NumberInput(
            attrs={
                "class": "form-control number-input",
                "placeholder": "550123456",
                "type": "number",
            }
            ),
        "date": forms.DateInput(
            attrs={
                "class": "form-control datetimepicker-input",
                "data-target": "#datetimepicker4",
                "placeholder": "Date",
                "type": "date",
            }
        ),
        "comment": forms.Textarea(attrs={"cols": 30, "rows": 3}),
        "time": forms.TimeInput(
            attrs={
                "class": "form-control timepicker-input",
                "data-target": "#datetimepicker3",
                "placeholder": "Time",
                "type": "time",
            }
        ),
        "amount_humans": forms.Select(
            attrs={"class": "form-control", "id": "selectPerson"}
        ),
        }