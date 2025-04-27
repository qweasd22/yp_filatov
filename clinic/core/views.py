from django.shortcuts import render
from .models import Doctor, Patient, Visit
from .forms import DoctorForm, PatientForm, VisitForm
from django.views.generic import DeleteView
from django.urls import reverse_lazy
from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse

def doctors_list(request):
    doctors = Doctor.objects.all()
    return render(request, 'doctors.html', {'doctors': doctors})

def doctor_detail(request, pk):
    doctor = get_object_or_404(Doctor, pk=pk)
    return render(request, 'doctor_detail.html', {'doctor': doctor})

def doctor_form(request, pk=None):
    doctor = get_object_or_404(Doctor, pk=pk) if pk else None
    if request.method == 'POST':
        form = DoctorForm(request.POST, instance=doctor)
        if form.is_valid():
            form.save()
            return redirect('doctors')
    else:
        form = DoctorForm(instance=doctor)
    
    context = {
        'form': form,
        'is_edit': pk is not None  # Добавляем флаг редактирования
    }
    return render(request, 'doctor_form.html', context)

class DoctorDelete(DeleteView):
    model = Doctor
    success_url = reverse_lazy('doctors')
    template_name = 'confirm_delete.html'

def index(request):
    return render(request, 'index.html')
# Patients
def patients_list(request):
    patients = Patient.objects.all()
    return render(request, 'patients.html', {'patients': patients})

def patient_detail(request, pk):
    patient = get_object_or_404(Patient, pk=pk)
    return render(request, 'patient_detail.html', {'patient': patient})

def patient_form(request, pk=None):
    patient = get_object_or_404(Patient, pk=pk) if pk else None
    if request.method == 'POST':
        form = PatientForm(request.POST, instance=patient)
        if form.is_valid():
            form.save()
            return redirect('patients')
    else:
        form = PatientForm(instance=patient)
    return render(request, 'patient_form.html', {'form': form})

class PatientDelete(DeleteView):
    model = Patient
    success_url = reverse_lazy('patients')
    template_name = 'confirm_delete.html'

from django.http import JsonResponse

def patient_discount_api(request, pk):
    try:
        patient = Patient.objects.get(pk=pk)
        discounts = {
            'pensioner': 10,
            'veteran': 15,
            'disabled': 20
        }
        return JsonResponse({'discount': discounts.get(patient.discount_category, 0)})
    except Patient.DoesNotExist:
        return JsonResponse({'error': 'Patient not found'}, status=404)
# Visits
def visits_list(request):
    visits = Visit.objects.select_related('doctor', 'patient').all()
    return render(request, 'visits.html', {'visits': visits})

def visit_detail(request, pk):
    visit = get_object_or_404(Visit, pk=pk)
    return render(request, 'visit_detail.html', {'visit': visit})

def visit_form(request, pk=None):
    visit = get_object_or_404(Visit, pk=pk) if pk else None
    if request.method == 'POST':
        form = VisitForm(request.POST, instance=visit)
        if form.is_valid():
            # Принудительно устанавливаем скидку из категории пациента
            patient = form.cleaned_data.get('patient')
            if patient:
                form.instance.discount = patient.get_discount_value()
            form.save()
            return redirect('visits')
    else:
        form = VisitForm(instance=visit)
    
    return render(request, 'visit_form.html', {'form': form})

class VisitDelete(DeleteView):
    model = Visit
    success_url = reverse_lazy('visits')
    template_name = 'confirm_delete.html'

def edit_doctor(request, pk):
    return doctor_form(request, pk)

def edit_patient(request, pk):
    return patient_form(request, pk)

def edit_visit(request, pk):
    return visit_form(request, pk)