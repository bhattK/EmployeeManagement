from django.contrib import admin
from employee.models import Employee

#admin.site.register(Employee)
# Register your models here.

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['id','fname','lname', 'desig', 'location', 'manager']