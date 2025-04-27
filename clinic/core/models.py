from django.db import models

class Doctor(models.Model):
    CATEGORY_CHOICES = [
        ('1', 'Первая'),
        ('2', 'Вторая'),
        ('3', 'Высшая')
    ]
    
    last_name = models.CharField("Фамилия", max_length=50)
    first_name = models.CharField("Имя", max_length=50)
    middle_name = models.CharField("Отчество", max_length=50)
    specialty = models.CharField("Специальность", max_length=100)
    category = models.CharField("Категория", max_length=1, choices=CATEGORY_CHOICES)

    def __str__(self):
        return f"{self.last_name} {self.first_name[0]}.{self.middle_name[0]}."

class Patient(models.Model):
    DISCOUNT_CATEGORIES = [
        ('none', 'Без скидки'),
        ('pensioner', 'Пенсионер - 10%'),
        ('veteran', 'Ветеран - 15%'),
        ('disabled', 'Инвалид - 20%'),
    ]
    
    last_name = models.CharField("Фамилия", max_length=50)
    first_name = models.CharField("Имя", max_length=50)
    middle_name = models.CharField("Отчество", max_length=50)
    birth_year = models.IntegerField("Год рождения")
    discount_category = models.CharField(
        "Категория скидки",
        max_length=10,
        choices=DISCOUNT_CATEGORIES,
        default='none'
    )
    @property
    def full_name(self):
        return f"{self.last_name} {self.first_name} {self.middle_name}"
    
    def __str__(self):
        return f"{self.last_name} {self.first_name} {self.middle_name}"
    def get_discount_value(self):
        discounts = {
            'pensioner': 10,
            'veteran': 15,
            'disabled': 20
        }
        return discounts.get(self.discount_category, 0)

class Visit(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    date = models.DateField("Дата обращения")
    diagnosis = models.TextField("Диагноз")
    base_cost = models.DecimalField("Базовая стоимость", max_digits=10, decimal_places=2)
    discount = models.DecimalField("Скидка (%)", max_digits=5, decimal_places=2, default=0)
    
    def __str__(self):
        return f"{self.doctor} - {self.patient}"
    @property
    def final_cost(self):
        return self.base_cost * (1 - self.discount / 100)