from django.contrib import admin
from service.models import Service
# Register your models here.
class ServiceAdmin(admin.ModelAdmin):
    list_display=('user_name','user_email','user_desc')
    

admin.site.register(Service,ServiceAdmin)