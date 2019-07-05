from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from prescription.models import Prescription
from .serializers import PrescriptionSerializer


class PrescriptionList(APIView):

    def get(self, request, id=None):

        prescription_list = Prescription.objects.all().order_by('-id')

        prescription_serialization = PrescriptionSerializer(prescription_list, many=True)

        return Response(prescription_serialization.data)

    