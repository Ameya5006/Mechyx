from rest_framework.response import Response
from rest_framework.views import APIView


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
            }
        )
