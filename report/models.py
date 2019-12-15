from django.db import models

from core.models import UserProfile
from dashboard.models import Department


class ReportType(models.Model):
    WEEK = 1
    TERM = 2
    YEAR = 3
    TIME_CHOICES = (
        (WEEK, 'Icyumweru'),
        (TERM, 'Igihembwe'),
        (YEAR, 'Umwaka'),
    )
    report_type = models.CharField(max_length=300)
    igihe_itangirwa = models.PositiveSmallIntegerField(choices=TIME_CHOICES)
    owner = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    deadline = models.DateTimeField()
    department = models.ForeignKey(Department, on_delete=models.CASCADE)


class Report(models.Model):
    report_type = models.ForeignKey(ReportType, on_delete=models.CASCADE)
    file = models.FileField()
    date = models.DateTimeField()
