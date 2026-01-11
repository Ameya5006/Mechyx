from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api.views import (
    ComponentViewSet,
    HealthView,
    IssueViewSet,
    RootView,
    ServiceNoteViewSet,
    SupplierViewSet,
)

router = DefaultRouter()
router.register("components", ComponentViewSet, basename="component")
router.register("suppliers", SupplierViewSet, basename="supplier")
router.register("issues", IssueViewSet, basename="issue")
router.register("service-notes", ServiceNoteViewSet, basename="service-note")

urlpatterns = [
    path("", RootView.as_view(), name="api-root"),
    path("health/", HealthView.as_view(), name="api-health"),
    path("", include(router.urls)),
]
