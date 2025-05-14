from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


class Commission(models.Model):
    title = models.CharField(max_length=255)
    # TODO author = foreign key
    description = models.TextField()

    class StatusChoices(models.TextChoices):
        OPEN = "O"
        FULL = "F"
        COMPLETED = "C"
        DISCONTINUED = "D"
    status = models.CharField(
        max_length=12,
        choices=StatusChoices,
        default=StatusChoices.OPEN,
    )

    created_on = models.DateTimeField(auto_now_add=True, editable=False)
    updated_on = models.DateTimeField(auto_now=True, editable=False)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('commissions:commission', args=[str(self.pk)])

    class Meta:
        ordering = ['created_on']


class Job(models.Model):
    commission = models.ForeignKey(
        Commission,
        on_delete=models.CASCADE,
        related_name='jobs'
    )
    role = models.CharField(max_length=255)
    manpower_required = models.PositiveIntegerField()

    class StatusChoices(models.TextChoices):
        OPEN = "O"
        FULL = "F"
    status = models.CharField(
        max_length=4,
        choices=StatusChoices,
        default=StatusChoices.OPEN,
    )

    def __str__(self):
        return f"[{self.commission}] {self.role}"

    def get_absolute_url(self):
        return reverse('commissions:commission', args=[str(self.commission.pk)])

    class Meta:
        ordering = ["-status", "-manpower_required", "role"]


class JobApplication(models.Model):
    job = models.ForeignKey(
        Job,
        on_delete=models.CASCADE,
        related_name='job_applications'
    )
    # TODO Applicant foreign key Profile

    class StatusChoices(models.TextChoices):
        PENDING = "A", _("Pending")
        ACCEPTED = "B", _("Accepted")
        REJECTED = "C", _("Rejected")
    status = models.CharField(
        max_length=8,
        choices=StatusChoices,
        default=StatusChoices.PENDING,
    )

    applied_on = models.DateTimeField(auto_now_add=True, editable=False)

    def __str__(self):
        return f"[{self.commission}] {self.status}"

    def get_absolute_url(self):
        return reverse('commissions:commission', args=[str(self.commission.pk)])

    class Meta:
        ordering = ["status", "-applied_on"]
