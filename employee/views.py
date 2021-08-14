from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from rest_framework import generics
from employee.models import Employee
from employee.serializer import EmployeeSerializer
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.

class EmployeeList(generics.ListAPIView):
    """
    Returns a list of all employees in the system
    """
    #define queryset
    queryset = Employee.objects.all()
    #define serializer to be used
    serializer_class = EmployeeSerializer
    filter_backends = [SearchFilter]
    # search_fields = ['manager', 'location']
    search_fields = ['^desig']

class EmployeeCreate(generics.CreateAPIView):
    """
    Create a new employee in the system
    """
    queryset = Employee
    serializer_class = EmployeeSerializer

class EmployeeRetrieve(generics.RetrieveAPIView):
    """
    Retrieve an individual employee in the system
    """
    queryset = Employee
    serializer_class = EmployeeSerializer

class EmployeeUpdate(generics.UpdateAPIView):
    """
    Updates a employee in the system
    """
    queryset = Employee
    serializer_class = EmployeeSerializer

class EmployeeDelete(generics.DestroyAPIView):
    """
    Deletes a employee in the system
    """
    queryset = Employee
    serializer_class = EmployeeSerializer


    #queryset = Employee.objects.filter(location='delhi')
    # filterset_fields = ['manager']
    # filterset_fields = ['id', 'desig']
    # def get_queryset(self):
        # current user
        # user = self.request.user 
        # return Employee.objects.filter(manager=user)