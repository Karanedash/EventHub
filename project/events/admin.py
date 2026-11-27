from django.contrib import admin
from .models import Event, Registration
# Register your models here.
class AdminEvent(admin.ModelAdmin):
    search_fields = ("title", "location")
    list_filter = ["date"]


admin.site.register(Event, AdminEvent)


class AdminRegister(admin.ModelAdmin):
    list_display = ["event", "name", "email", "phone", "comment", "created_at", "status"]
    readonly_fields = ["event", "name", "email", "phone", "comment", "created_at"]
    search_fields = ("name", "email")

    def has_add_permission(self, request):
        return False


admin.site.register(Registration, AdminRegister)