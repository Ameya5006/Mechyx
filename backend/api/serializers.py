from rest_framework import serializers

from api.models import Component, Issue, ServiceNote, Supplier


class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = [
            "id",
            "name",
            "tier",
            "risk_score",
            "region",
            "created_at",
        ]


class ComponentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Component
        fields = [
            "id",
            "name",
            "subsystem",
            "design_owner",
            "created_at",
        ]


class IssueSerializer(serializers.ModelSerializer):
    component_detail = ComponentSerializer(source="component", read_only=True)
    supplier_detail = SupplierSerializer(source="supplier", read_only=True)

    class Meta:
        model = Issue
        fields = [
            "id",
            "title",
            "description",
            "severity",
            "status",
            "detected_at",
            "component",
            "supplier",
            "component_detail",
            "supplier_detail",
            "created_at",
        ]


class ServiceNoteSerializer(serializers.ModelSerializer):
    issue_detail = IssueSerializer(source="issue", read_only=True)

    class Meta:
        model = ServiceNote
        fields = [
            "id",
            "issue",
            "issue_detail",
            "source",
            "symptom_summary",
            "raw_note",
            "technician",
            "mileage",
            "created_at",
        ]
