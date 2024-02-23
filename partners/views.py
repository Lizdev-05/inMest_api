from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views import View
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from partners.models import *
from partners.serializers import *



# Create your views here.

def json_response(request):
    return HttpResponse("Hello, world. You're at the partners index.")


def http_response(request):
    return HttpResponse("<h1>Hello, world. You're at the partners index.</h1>")

def say_hello(request):
    return HttpResponse("<h1>Hello, world. This is the first route in django class.</h1>")


# view function that is called user_profile and returns a json response which includes name: Oyinlade, email: ojesanmioyinlade@gmail.com, phone: 08012345678 and address: 123, Ikorodu road, Lagos
#  register the view function on a path called profile in the partners/urls.py file

user_profile = {
    "name": "Oyinlade",
    "email": "ojesanmioyinlade@gmail.com",
    "phone": "08012345678",
    "address": "123, Ikorodu road, Lagos"
}

def profile(request):
    user_name = f"<h1> Name: {user_profile['name']} </h1>"
    user_email = f"<h1> Email: {user_profile['email']} </h1>"
    user_phone = f"<h1> Phone: {user_profile['phone']} </h1>"
    user_address = f"<h1> Address: {user_profile['address']} </h1>"
    return HttpResponse(user_name + user_email + user_phone + user_address)

def profile_two(request):
    return JsonResponse(user_profile )  

# Write  afunction called filter_queries that that receives query_id  through the url
# return a json resonse data with the following data id, name, title, descriptionn and submited_by
# the id should be recieved from the url and the rest of the data should be retrieved from the following dictionary

query_data = [
    {
        "id": 1,
        "name": "Oyinlade",
        "title": "Django class",
        "description": "I am learning django",
        "submited_by": "Oyinlade"
    },
   {
        "id": 2,
        "name": "Oyinlade",
        "title": "February fitnes",
        "description": "Daily work out for the 20mins throughout February!",
        "submited_by": "Oyinlade"
    },
    {
        "id": 3,
        "name": "March",
        "title": "Focus on health",
        "description": "Eat no meat for the entire month",
        "submited_by": "Oyinlade"
    }
]

def filter_queries(request, query_id):
    

    for query in query_data:
        if query['id'] == query_id:
            return JsonResponse(query)
    return HttpResponse("Query not found")
        

def all_queries(request):
    return JsonResponse(query_data, safe=False)


# class based view`

class QueryView(View):
    query_data = [
    {
        "id": 1,
        "name": "Oyinlade",
        "title": "Django class",
        "description": "I am learning django",
        "submited_by": "Oyinlade"
    },
   {
        "id": 2,
        "name": "Oyinlade",
        "title": "February fitnes",
        "description": "Daily work out for the 20mins throughout February!",
        "submited_by": "Oyinlade"
    },
    {
        "id": 3,
        "name": "March",
        "title": "Focus on health",
        "description": "Eat no meat for the entire month",
        "submited_by": "Oyinlade"
    }
]
    def get(self, request):
        # return JsonResponse(self.query_data, safe=False)
                return JsonResponse({"result": self.query_data})
    
    def post(self, request):
         return JsonResponse({"status": "Ok"})


@api_view(["GET"])
def fetch_class_schedule(request):
#  Retrieve from DB all class schedule
  queryset = ClassSchedule.objects.all()

#  Return queryset result as response
#    Transform/serialize the queryset result to json and send as response
 
  serializer = ClassScheduleSerializer(queryset, many=True)
# Respond to the request
  return Response({"data": serializer.data}, status.HTTP_200_OK)




    
@api_view(['POST'])
def create_class_schedule(request):
  title = request.data.get("title")
  description = request.data.get("description")
  start_date_and_time = request.data.get("start_date_and_time")
  end_date_and_time = request.data.get("end_date_and_time")
  cohort_id = request.data.get("cohort_id")
  venue = request.data.get("venue")
  repeat_frequency = request.data.get("   repeat_frequency")
  is_repeated = request.data.get("is_repeated")
  venue = request.data.get("venue")

  if not title:
      return Response({"message": "My friend, send me title!!!"})