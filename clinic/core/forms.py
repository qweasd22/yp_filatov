from django import forms
from .models import Doctor, Patient, Visit, PatientProfile
from django.contrib.auth.forms import UserCreationForm

class DoctorForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = '__all__'

        widgets = {
            'birth_year': forms.NumberInput(attrs={'min': 1900, 'max': 2100}),
            

        }


class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = '__all__'
        widgets = {
            'birth_year': forms.NumberInput(attrs={'min': 1900, 'max': 2100}),
        }

class VisitForm(forms.ModelForm):
    class Meta:
        model = Visit
        fields = '__all__'
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'discount': forms.HiddenInput()  # Скрываем поле скидки
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['discount'].required = False

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance.pk:
            self.initial['discount'] = self.instance.discount
        else:
            self.initial['discount'] = 0

    def clean(self):
        cleaned_data = super().clean()
        patient = cleaned_data.get('patient')
        if patient:
            discounts = {
                'pensioner': 10,
                'veteran': 15,
                'disabled': 20
            }
            cleaned_data['discount'] = discounts.get(patient.discount_category, 0)
        return cleaned_data
    

class PatientSignUpForm(UserCreationForm):
    birth_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    phone = forms.CharField(max_length=20)
    
    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ('email', 'first_name', 'last_name')

    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
            PatientProfile.objects.create(
                user=user,
                birth_date=self.cleaned_data['birth_date'],
                phone=self.cleaned_data['phone']
            )
        return user