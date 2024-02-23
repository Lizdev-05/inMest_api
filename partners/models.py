from django.db import models

# Create your models here.
class Course(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField( default='N/A', blank=True, null=True)
    date_created = models.DateTimeField( auto_now_add=True, blank=True, null=True)
    date_updated = models.DateTimeField( auto_now=True, blank=True, null=True)

    def __str__(self):
        return f"{self.name} - {self.description}"
    
class ClassSchedule(models.Model):  
    title = models.CharField(max_length=100)
    description = models.TextField( default='N/A', blank=True, null=True)
    course = models.ForeignKey('users.Cohort', on_delete=models.CASCADE, related_name='class_schedules', blank=True, null=True )
    facilitator = models.ForeignKey('users.IMUser', on_delete=models.CASCADE, related_name='facilitated_classes', blank=True, null=True)
    start_date_and_time = models.DateTimeField()
    end_date_and_time = models.DateTimeField()
    is_repeated = models.BooleanField(default=False)
    repeat_frequency = models.CharField(max_length=100, default='N/A', blank=True, null=True)
    is_active = models.BooleanField(default=True)
    organizer = models.ForeignKey('users.IMUser', on_delete=models.CASCADE, related_name='organizer')
    cohort = models.ForeignKey('users.Cohort', on_delete=models.CASCADE, related_name='cohort')
    venue = models.CharField(max_length=100, default='N/A', blank=True, null=True)
    date_created = models.DateTimeField( auto_now_add=True, blank=True, null=True)
    date_updated = models.DateTimeField( auto_now=True, blank=True, null=True)

    def __str__(self):
        return f"{self.title} - {self.description} - {self.start_date_and_time} - {self.end_date_and_time} - {self.is_repeated} - {self.repeat_frequency} - {self.is_active} - {self.organizer} - {self.cohort} - {self.venue}"
    
class ClassAttendance(models.Model):
    class_schedule = models.ForeignKey(ClassSchedule, on_delete=models.CASCADE)
    attendee = models.ForeignKey('users.IMUser', on_delete=models.CASCADE, related_name='attended_class_attendances')
    author = models.ForeignKey('users.IMUser', on_delete=models.CASCADE, related_name='authored_class_attendances')
    is_present = models.BooleanField(default = True)
    date_modified = models.DateTimeField(auto_now=True)
    date_created= models.DateTimeField(auto_now=True)

class Query(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(default='N/A', blank=True, null=True)
    submitted_by = models.ForeignKey('users.IMUser', on_delete=models.CASCADE, related_name='submitted_queries')
    assigned_to = models.ForeignKey('users.IMUser', on_delete=models.CASCADE, related_name='assigned_queries')
    resolution_status = models.CharField(max_length=100, choices=[
        ('PENDING', 'PENDING'),
        ('IN_PROGRESS', 'IN_PROGRESS'),
        ('DECLINED', 'DECLINED'),
        ('RESOLVED', 'RESOLVED')
    ])
    date_created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    date_updated = models.DateTimeField(auto_now=True, blank=True, null=True)
    author = models.ForeignKey('users.IMUser', on_delete=models.CASCADE, related_name='authored_queries')

class QueryComment(models.Model):
    query = models.ForeignKey(Query, on_delete=models.CASCADE)
    comment = models.TextField(default='N/A', blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    date_updated = models.DateTimeField(auto_now=True, blank=True, null=True)
    author = models.ForeignKey('users.IMUser', on_delete=models.CASCADE, related_name='authored_query_comments')
