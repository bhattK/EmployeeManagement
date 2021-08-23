"""EmployeeManagement URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from employee.views import EmployeeList, EmployeeCreate,EmployeeRetrieve, EmployeeUpdate, EmployeeDelete
from rest_framework import permissions
from rest_framework.schemas import get_schema_view
from rest_framework.documentation import include_docs_urls
from django.views.generic import TemplateView

urlpatterns = [
    path('', TemplateView.as_view(template_name='index.html')),
    path('api/employees/', EmployeeList.as_view()),
    path('api/employee/create', EmployeeCreate.as_view()),
    # path('api/employee/retrieve/<int:pk>', EmployeeRetrieve.as_view()),
    path('api/employee/update/<int:pk>', EmployeeUpdate.as_view()),
    path('api/employee/delete/<int:pk>', EmployeeDelete.as_view()),
    path('admin/', admin.site.urls),
    path('openapi', get_schema_view(
        title="Employee_CRUD_API",
        description="Basic API for CRUD operations"
    ), name='openapi-schema'),
    # path('swagger-ui/', TemplateView.as_view(
    #     template_name='doc.html',
    #     extra_context={'schema_url':'openapi-schema'}
    # ), name='api_doc'),
]
