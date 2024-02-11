from django.db import models

# Create your models here.
# Q1. In your models.py of users app; create the following models and add them to your admin.py
# IMUser (first_name, last_name, is_active, user_type [EIT, TEACHING_FELLOW, ADMIN_STAFF, ADMIN], date_created). Feel free to add extra fields you can think of. Custom user  management/auth implementation will be done later
# Cohort(name, description, year, start_date, end_date, is_active, date_created, date_modified, author [should reference IMUser model])
# CohorMember(cohort[Should reference Cohort model], member [should reference IMUser], is_active, date_created, date_modified, author [should reference IMUser model])


class IMUser(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    user_type = models.CharField(max_length=100, choices=[
        ('EIT', 'EIT'),
        ('TEACHING_FELLOW', 'TEACHING_FELLOW'),
        ('ADMIN_STAFF', 'ADMIN_STAFF'),
        ('ADMIN', 'ADMIN')
    ])
    date_created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    date_updated = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} - {self.last_name} - {self.is_active} - {self.user_type} - {self.date_created} - {self.date_updated}"
    
class Cohort(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    year = models.CharField(max_length=100)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    is_active = models.BooleanField(default=True)
    date_created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    date_updated = models.DateTimeField(auto_now=True, blank=True, null=True)
    author = models.ForeignKey(IMUser, on_delete=models.CASCADE, related_name='authored_cohorts')

class CohortMember(models.Model):
    cohort = models.ForeignKey(Cohort, on_delete=models.CASCADE)
    member = models.ForeignKey(IMUser, on_delete=models.CASCADE, related_name='cohorts')
    is_active = models.BooleanField(default=True)
    date_created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    date_updated = models.DateTimeField(auto_now=True, blank=True, null=True)
    author = models.ForeignKey(IMUser, on_delete=models.CASCADE, related_name='authored_cohort_members')
