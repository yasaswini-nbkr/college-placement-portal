from django.db import models
from django.contrib.auth.models import User


class StudentProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=15)
    department = models.CharField(max_length=50)
    roll_number = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return self.user.get_full_name()


class Job(models.Model):
    company_name = models.CharField(max_length=100)
    job_role = models.CharField(max_length=100)
    description = models.TextField()
    location = models.CharField(max_length=100)
    salary = models.CharField(max_length=100)
    eligibility = models.CharField(max_length=200)
    deadline = models.DateField()

    def __str__(self):
        return f"{self.company_name} - {self.job_role}"

class Application(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Selected', 'Selected'),
        ('Rejected', 'Rejected'),
    ]

    student = models.ForeignKey(User, on_delete=models.CASCADE)
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    applied_on = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')

    def __str__(self):
        return f"{self.student.username} - {self.job.company_name}"