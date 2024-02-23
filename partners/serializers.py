from rest_framework import serializers
from users.serializers import CohortSerializer, UserSerializer

# Create your serializers here.
class CourseSerializer(serializers.Serializer):
    name = serializers.CharField()
    description = serializers.CharField()
    date_created = serializers.DateTimeField( )
    date_updated = serializers.DateTimeField( )
    

class ClassScheduleSerializer(serializers.Serializer):  
    title = serializers.CharField()
    description = serializers.CharField()
    organizer = UserSerializer(many = False )
    cohort = CohortSerializer(many = False )
    venue = serializers.CharField()
    start_date_and_time = serializers.DateTimeField()
    end_date_and_time = serializers.DateTimeField()
    is_repeated = serializers.BooleanField()
    repeat_frequency = serializers.CharField()
    is_active = serializers.BooleanField()
    date_created = serializers.DateTimeField( )
    date_updated = serializers.DateTimeField()

   

    
class ClassAttendanceSerializer(serializers.Serializer):
    class_schedule = serializers.IntegerField( )
    attendee = UserSerializer(many = False )
    author = serializers.IntegerField()

class QuerySerializer(serializers.Serializer):
    title = serializers.CharField()
    description = serializers.CharField()
    author = serializers.IntegerField()

class QueryCommentSerializer(serializers.Serializer):
    query = serializers.IntegerField( )
    comment = serializers.CharField()
    author = serializers.IntegerField( )
