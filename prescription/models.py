from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Prescription(models.Model):

    GENDER_STATUS = (
        ('Male', 'MALE'),
        ('Female', 'FEMALE'),
        ('Other', 'OTHER'),
    )

    prescription_date = models.DateField(default=timezone.now, blank=False)
    patient_name = models.CharField(max_length=50, blank=False)
    patient_age = models.PositiveIntegerField(blank=False)
    patient_gender = models.CharField(max_length=10, choices=GENDER_STATUS, blank=False, default='OTHER')
    diagnosis = models.CharField(max_length=100000)
    medicines = models.CharField(max_length=100000)
    next_visit_date = models.DateTimeField(auto_now_add=False, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=False, null=True)

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.patient_name
