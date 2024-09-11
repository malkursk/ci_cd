"""Description"""

from django.db import models


class Employee(models.Model):
    """Class description"""

    fio = models.CharField(max_length=255)
    job = models.CharField(max_length=255)
    phone = models.CharField(max_length=20, null=True)
    burn = models.DateField(null=True)
    email = models.EmailField(null=True)
    department = models.ForeignKey(
        "company.Department",
        null=True,
        related_name="employees",
        on_delete=models.CASCADE,
    )


class Department(models.Model):
    """Class description"""

    name = models.CharField(max_length=255)
    stage = models.PositiveIntegerField()
    office = models.ForeignKey(
        "company.Office",
        null=True,
        related_name="departments",
        on_delete=models.SET_NULL,
    )


class Office(models.Model):
    """Class description"""

    short_name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
