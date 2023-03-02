# from django.contrib import admin
# from .models import Employee, Role, EmployeeUser
# from django.contrib.auth.admin import UserAdmin
# from django.utils.translation import gettext_lazy as _
# from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin
# from django.urls import reverse
# from django.utils.html import format_html
# from .views import register_employee


# class EmployeeAdmin(UserAdmin):
#     list_display = ('email')
#     actions = ['send_login_credentials']

#     def send_login_credentials(self, request, queryset):
#         for employee in queryset:
#             register_employee(request, email=employee.email)
#         self.message_user(request, 'Login credentials sent successfully.')
#     send_login_credentials.short_description = "Send login credentials to selected employees"


# class EmployeeAdmin(UserAdmin):
#     pass

# admin.site.register(Employee)
# admin.site.register(Role)
# admin.site.register(EmployeeUser)


from django.contrib import admin
from .models import Employee, Role


admin.site.register(Employee)
admin.site.register(Role)
