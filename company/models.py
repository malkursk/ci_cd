from django.db import models

class Employee(models.Model):
    fio = models.CharField(max_length=255)
    job = models.CharField(max_length=255)
    phone = models.CharField(max_length=20, null=True)
    burn = models.DateField(null=True)
    email = models.EmailField(null=True)
    department = models.ForeignKey(
        'company.Department',
        null=True,
        related_name='employees',
        on_delete=models.CASCADE,
    )


class Department(models.Model):
    name = models.CharField(max_length=255)
    stage = models.PositiveIntegerField()
    office = models.ForeignKey(
        'company.Office', 
        null=True, 
        related_name='departments', 
        on_delete=models.SET_NULL,
    )

class Office(models.Model):
    short_name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)

