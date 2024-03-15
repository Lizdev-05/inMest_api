from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework.response import Response


class AuthSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    auth_token = serializers.CharField(read_only=True)
    first_name = serializers.CharField()
    last_name = serializers.CharField()

class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()



class CohortSerializer(serializers.Serializer):
    name = serializers.CharField()
    description = serializers.CharField()
    year = serializers.CharField()
    start_date = serializers.DateTimeField()
    end_date = serializers.DateTimeField()
    author = UserSerializer(many = False)


class CohortMemberSerializer(serializers.Serializer):
    cohort = CohortSerializer(many = False)
    member = UserSerializer(many = False)

class QuerySerializer(serializers.ModelSerializer):
    class Meta:
        model = Query
        fields = '_all_'

class ClassScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassSchedule
        fields = '_all_'


   

