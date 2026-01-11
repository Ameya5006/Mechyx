from django.contrib import admin

from api.models import Component, Issue, ServiceNote, Supplier


@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = ("name", "tier", "risk_score", "region", "created_at")
    search_fields = ("name", "region")


@admin.register(Component)
class ComponentAdmin(admin.ModelAdmin):
    list_display = ("name", "subsystem", "design_owner", "created_at")
    search_fields = ("name", "subsystem", "design_owner")


@admin.register(Issue)
class IssueAdmin(admin.ModelAdmin):
    list_display = ("title", "severity", "status", "detected_at", "component")
    list_filter = ("status", "severity")
    search_fields = ("title", "description")


@admin.register(ServiceNote)
class ServiceNoteAdmin(admin.ModelAdmin):
    list_display = ("issue", "source", "symptom_summary", "technician", "mileage")
    search_fields = ("symptom_summary", "raw_note", "technician")
