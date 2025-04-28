from rest_framework import serializers
from .models import Doctor, Patient, Visit

class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = '__all__'

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = '__all__'

class VisitSerializer(serializers.ModelSerializer):
    doctor = serializers.PrimaryKeyRelatedField(queryset=Doctor.objects.all())
    patient = serializers.PrimaryKeyRelatedField(queryset=Patient.objects.all())
    
    # Дополнительные поля только для чтения
    doctor_details = serializers.SerializerMethodField()
    patient_details = serializers.SerializerMethodField()

    class Meta:
        model = Visit
        fields = '__all__'
        extra_fields = ['doctor_details', 'patient_details']

    def get_doctor_details(self, obj):
        return {
            "id": obj.doctor.id,
            "name": f"{obj.doctor.last_name} {obj.doctor.first_name}"
        }

    def get_patient_details(self, obj):
        return {
            "id": obj.patient.id,
            "name": f"{obj.patient.last_name} {obj.patient.first_name}"
        }