from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view

from rest_framework.response import Response

from app.seralizer import *

from app.models import *

@api_view()
def employee(request):
    EQS=Employee.objects.all()
    EOD=EmployeeSF(EQS,many=True)
    return Response(EOD.data)


    