from django.urls import path

from .views import (

    add_prescription,
    filtered_prescriptions,
    prescription_details,
    edit,
    delete,

)


app_name = 'prescription'


urlpatterns = [


    path('add-prescription/', add_prescription, name='add-prescription'),

    path('filtered-prescriptions/<int:id>/', filtered_prescriptions, name='filtered-prescriptions'),

    path('prescription-details/<int:id>/', prescription_details, name='prescription-details'),

    path('edit/<int:id>/', edit, name='edit'),

    path('delete/<int:id>', delete, name='delete'),


]
