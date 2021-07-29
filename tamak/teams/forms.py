from django import forms
from django.forms import widgets
from .models import Teams

class CreateTeamsForm(forms.ModelForm):
    class Meta:
        model = Teams
        fields = ['user', 'position', 'education', 'experience', 'companies']

        widgets = {
        "user": forms.Select(
            attrs={"class": "form-control",}
        ),
        "position": forms.Select(
            attrs={"class": "form-control",}
        ),
        "education": forms.Select(
            attrs={"class": "form-control"}
        ),
        "experience": forms.TextInput(
            attrs={"class": "form-control",}
        ),
        "companies": forms.TextInput(
            attrs={"class": "form-control",}
        ),
        }


# from django import forms
# from django.forms import widgets
# from .models import Teams

# class CreateReservationsForm(forms.ModelForm):
#     class Meta:
#         model = Teams
#         exclude = ['user', 'date_registered']

#         widgets = {
#         "position": forms.NumberInput(attrs={"class": "form-control number-input","placeholder": "550123456", "type": "number",}),
#         "education": forms.DateInput(attrs={"class": "form-control datetimepicker-input", "data-target": "#datetimepicker4","placeholder": "Date", "type": "date", 0}),
#         "experience": forms.Textarea(attrs={"cols": 30, "rows": 3}),
#         "companies": forms.TimeInput(attrs={"class": "form-control timepicker-input", "data-target": "#datetimepicker3","placeholder": "Time", "type": "time", 0}),
        
#         "amount_humans": forms.Select(attrs={"class": "form-control", "id": "selectPerson"}),}