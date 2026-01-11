from django.db import models


class Supplier(models.Model):
    name = models.CharField(max_length=200)
    tier = models.CharField(max_length=50)
    risk_score = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    region = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name


class Component(models.Model):
    name = models.CharField(max_length=200)
    subsystem = models.CharField(max_length=120)
    design_owner = models.CharField(max_length=120)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name


class Issue(models.Model):
    STATUS_CHOICES = [
        ("open", "Open"),
        ("investigating", "Investigating"),
        ("mitigated", "Mitigated"),
        ("closed", "Closed"),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField()
    severity = models.CharField(max_length=20)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="open")
    detected_at = models.DateField()
    component = models.ForeignKey(
        Component, on_delete=models.CASCADE, related_name="issues"
    )
    supplier = models.ForeignKey(
        Supplier, on_delete=models.SET_NULL, null=True, blank=True, related_name="issues"
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title


class ServiceNote(models.Model):
    issue = models.ForeignKey(Issue, on_delete=models.CASCADE, related_name="notes")
    source = models.CharField(max_length=100)
    symptom_summary = models.CharField(max_length=200)
    raw_note = models.TextField()
    technician = models.CharField(max_length=120)
    mileage = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.issue.title} - {self.symptom_summary}"
