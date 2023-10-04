from django.contrib import admin
from .models import Service, Employee, Role


@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    list_display = ('Role', 'Active', 'Actualization')


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('Service', 'Icon', 'Active', 'Actualization')


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('Name', 'Role', 'Active', 'Actualization')
