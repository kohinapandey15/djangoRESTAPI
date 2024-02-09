from rest_framework.response import Response
from rest_framework.decorators import action
from django.shortcuts import render
from rest_framework import viewsets
from api.models import Company, Employee
from api.serializers import CompanySerializer, EmployeeSerializer
# Create your views here.
class CompanyViewSet(viewsets.ModelViewSet):
    queryset=Company.objects.all()
    serializer_class=CompanySerializer
    # if detail is true then it is must to pass primary key(pk)
    @action(detail=True, methods=['get'])  
    def employees(self,request,pk = None):
      try: 
        company = Company.objects.get(pk=pk)
        emps = Employee.objects.filter(company=company)
        emps_serializer = EmployeeSerializer(emps,many=True,context={'request' : request})
        return Response(emps_serializer.data)
      except Exception as e :
         print(e)
         return Response({
            'message' : 'Company might not exist !! Error'
         })
class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer