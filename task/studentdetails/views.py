from django.shortcuts import render

# Create your views here.
from rest_framework.viewsets import ModelViewSet
from .models import student
from .serializer import StudentSerializer
class StudentViewSet (ModelViewSet):
    serializer_class = StudentSerializer
    queryset = student.objects.all()