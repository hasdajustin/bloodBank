from django.contrib import admin
from .models import Donor

# Register your models here.
@admin.register(Donor)
class DonorAdmin(admin.ModelAdmin):
    list_display = ("full_name", "age", "blood_group",)
    list_filter = ("gender", "blood_group", "created_at")
    search_fields = ("full_name", "phone", "email")
    ordering = ("-created_at",)