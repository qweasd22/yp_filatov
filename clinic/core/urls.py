from django.urls import path
from .views import *

urlpatterns = [
    # Doctors
    path('doctors/', doctors_list, name='doctors'),
    path('doctor/add/', doctor_form, name='add_doctor'),
    path('doctor/<int:pk>/', doctor_detail, name='doctor_detail'),
    path('doctor/<int:pk>/edit/', doctor_form, name='edit_doctor'),
    path('doctor/<int:pk>/delete/', DoctorDelete.as_view(), name='delete_doctor'),
    
    # Patients
    path('patients/', patients_list, name='patients'),
    path('patient/add/', patient_form, name='add_patient'),
    path('patient/<int:pk>/', patient_detail, name='patient_detail'),
    path('patient/<int:pk>/edit/', patient_form, name='edit_patient'),
    path('patient/<int:pk>/delete/', PatientDelete.as_view(), name='delete_patient'),
    
    # Visits
    path('visits/', visits_list, name='visits'),
    path('visit/add/', visit_form, name='add_visit'),
    path('visit/<int:pk>/', visit_detail, name='visit_detail'),
    path('visit/<int:pk>/edit/', visit_form, name='edit_visit'),
    path('visit/<int:pk>/delete/', VisitDelete.as_view(), name='delete_visit'),
    path('doctor/<int:pk>/edit/', edit_doctor, name='edit_doctor'),
    path('patient/<int:pk>/edit/', edit_patient, name='edit_patient'),
    path('visit/<int:pk>/edit/', edit_visit, name='edit_visit'),
    path('',index, name='index'),
    path('api/patient-discount/<int:pk>/', patient_discount_api, name='patient_discount_api'),
    path('signup/', patient_signup, name='patient_signup'),
    path('doctors/', doctor_list, name='doctor_list'),
    path('appointment/<int:doctor_id>/', create_appointment, name='create_appointment'),
    path('', index, name='index'),
    path('', index, name='index'),
    path('admin/dashboard/', admin_dashboard, name='admin_dashboard'),
    path('doctors/', doctor_list, name='doctor_list'),
    # path('my-visits/', my_visits, name='my_visits'),
    
]