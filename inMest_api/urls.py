from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('partners.urls')),
    path('', include('users.urls')),

    path('api-auth/', include('rest_framework.urls'))
    

    # path('json_response/', json_response),
    # path('profile/', profile),
    # path('profile_two/', profile_two),
    # path('filter_queries/<int:query_id>/', filter_queries),
    

]
