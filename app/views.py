from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view,permission_classes

from rest_framework.response import Response

from rest_framework.permissions import IsAuthenticated

from app.seralizer import *

from app.models import *

@api_view()
@permission_classes([IsAuthenticated])
def employee(request):
    EQS=Employee.objects.all()
    EOD=EmployeeSF(EQS,many=True)
    return Response(EOD.data)


    