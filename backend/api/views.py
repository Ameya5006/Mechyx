from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from api.models import Component, Issue, ServiceNote, Supplier
from api.serializers import (
    ComponentSerializer,
    IssueSerializer,
    ServiceNoteSerializer,
    SupplierSerializer,
)


class HealthView(APIView):
    def get(self, request):
        return Response({"status": "ok", "service": "mechyx-backend"})


class RootView(APIView):
    def get(self, request):
        return Response(
            {
                "name": "Mechyx API",
                "modules": [
                    "issue-atlas",
                    "mechanic-signal-hub",
                    "design-impact-simulator",
                    "supplier-integrity-dashboard",
                    "assembly-guidance-generator",
                    "change-feedback-loop",
                ],
                "resources": [
                    "components",
                    "suppliers",
                    "issues",
                    "service-notes",
                ],
            }
        )


class SupplierViewSet(viewsets.ModelViewSet):
    queryset = Supplier.objects.all().order_by("name")
    serializer_class = SupplierSerializer


class ComponentViewSet(viewsets.ModelViewSet):
    queryset = Component.objects.all().order_by("name")
    serializer_class = ComponentSerializer


class IssueViewSet(viewsets.ModelViewSet):
    queryset = Issue.objects.select_related("component", "supplier").order_by(
        "-detected_at"
    )
    serializer_class = IssueSerializer


class ServiceNoteViewSet(viewsets.ModelViewSet):
    queryset = ServiceNote.objects.select_related("issue").order_by("-created_at")
    serializer_class = ServiceNoteSerializer
