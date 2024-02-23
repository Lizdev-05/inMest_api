from django.urls import path
from .views import *




# urlpatterns = [
#      path('json_response/', json_response),
#  ]
 
urlpatterns = [
    path('say_hello/', say_hello),
    path('http_response/', http_response),
    
    path('json_response/', json_response),
    path('profile/', profile),
    path('profile_two/', profile_two),

    path('filter_queries/<int:query_id>/', filter_queries),
    path('all_queries/', all_queries),

    # path("queries/", QueryView.as_view()),
path("queries/", QueryView.as_view(), name="query-view" ),\
path('schedule/fetch/', fetch_class_schedule)
]