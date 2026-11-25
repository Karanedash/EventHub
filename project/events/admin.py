from django.contrib import admin
from .models import Event, Registration
# Register your models here.
admin.site.register(Event)


class AdminRegister(admin.ModelAdmin):
    list_display = ["event", "name", "email", "phone", "comment", "created_at", "status"]
    readonly_fields = ["event", "name", "email", "phone", "comment", "created_at"]
    search_fields = ("name", "email")

    def has_add_permission(self, request):
        return False


admin.site.register(Registration, AdminRegister)