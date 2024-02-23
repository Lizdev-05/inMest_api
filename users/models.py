from django.db import models

from django.contrib.auth.models import AbstractUser


class IMUser(AbstractUser):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100, blank= True)
    is_active = models.BooleanField(default=True)
    phone_number = models.CharField(max_length=100, blank= True)
    user_type = models.CharField(max_length=100, choices=[
        ('EIT', 'EIT'),
        ('TEACHING_FELLOW', 'TEACHING_FELLOW'),
        ('ADMIN_STAFF', 'ADMIN_STAFF'),
        ('ADMIN', 'ADMIN')
    ])
    date_created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    date_updated = models.DateTimeField(auto_now=True, blank=True, null=True)
    date_modified = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} - {self.last_name} - {self.user_type}"
    
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



# Create 2022, 2023, 2024 cohorts

# from user.model import *
# IMUser.objects.all
# IMUser.objects..get(id=1)
# author = IMUser.objects.get(id=1)
# Cohort.objects.create(name="2022", description="2022 cohort", year="2022", start_date="2022-01-01", end_date="2022-12-31", author=author)
# Cohort.objects.create(name="2023", description="2023 cohort", year="2023", start_date="2023-01-01", end_date="2023-12-31", author=author)
# Cohort.objects.create(name="2024", description="2024 cohort", year="2024", start_date="2024-01-01", end_date="2024-12-31", author=author)
# create 4 different users
# IMUser.objects.create(username="eit1", first_name="EIT1", last_name="EIT1", user_type="EIT")  
# IMUser.objects.create(username="eit2", first_name="EIT2", last_name="EIT2", user_type="EIT")

# create 2 different cohort members
# cohort = Cohort.objects.get(id=1)
# member = IMUser.objects.get(id=1)
# CohortMember.objects.create(cohort=cohort, member=member, author=author)
# member = IMUser.objects.get(id=2)
# CohortMember.objects.create(cohort=cohort, member=member, author=author)
