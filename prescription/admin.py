from django.contrib import admin

from .models import Prescription


class PrescriptionAdmin(admin.ModelAdmin):
    list_display = ['id', 'patient_name', 'prescription_date', 'patient_age', 'patient_gender',
                    'diagnosis', 'medicines', 'next_visit_date', 'user']

    list_display_links = ['patient_name']

    search_fields = ['patient_name']


admin.site.register(Prescription, PrescriptionAdmin)


