from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User

from .forms import PrescriptionAddForm
from .models import Prescription

from source.views import home


#################################################################################################


@login_required
def add_prescription(request):

    if request.method == 'POST':
        form = PrescriptionAddForm(request.POST)

        if form.is_valid():
            form.save()

            messages.success(request, 'Prescription Added Successfully!')

            return redirect('prescription:filtered-prescriptions', id=request.user.id)

    else:
        form = PrescriptionAddForm()

    template = 'prescription/add_prescription.html'
    context = {'form': form}

    return render(request, template, context)

#################################################################################################


@login_required
def filtered_prescriptions(request, id=None):

    current_user = User.objects.get(id=id)
    filtered_prescriptions_by_user = Prescription.objects.filter(
        user=current_user)

    template = 'prescription/filtered_prescriptions.html'

    context = {'filtered_prescriptions_by_user': filtered_prescriptions_by_user}

    return render(request, template, context)

#################################################################################################


@login_required
def prescription_details(request, id=None):

    single_prescriptions_details = Prescription.objects.get(id=id)

    template = 'prescription/single_prescriptions_details.html'

    context = {'single_prescriptions_details': single_prescriptions_details}

    return render(request, template, context)

#################################################################################################


@login_required
def edit(request, id=None):

    query = Prescription.objects.get(id=id)
    form = PrescriptionAddForm(request.POST or None, instance=query)

    if request.method == 'POST':
        if form.is_valid():
            form.save()

            return redirect('prescription-details', id)
            # return redirect('prescription:prescription-details', id=request.user.id)

    context = {'form': form}
    template = 'prescription/edit.html'

    return render(request, template, context)

#################################################################################################


@login_required
def delete(request, id=None):

    delete_query = get_object_or_404(Prescription, id=id)

    if request.method == 'POST':

        delete_query.delete()
        return redirect('prescription:filtered-prescriptions', id=request.user.id)

    template = 'prescription/delete.html'
    context = {'delete_query': delete_query}
    return render(request, template, context)

#################################################################################################
