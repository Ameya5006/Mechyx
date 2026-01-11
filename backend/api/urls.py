from django.urls import path
from api.views import HealthView, RootView

urlpatterns = [
    path("", RootView.as_view(), name="api-root"),
    path("health/", HealthView.as_view(), name="api-health"),
]
