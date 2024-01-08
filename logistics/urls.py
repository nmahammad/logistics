from django.contrib import admin
from django.urls import path, include

app_name = "tracking"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('tracking.urls')),
    # path('orders/', include('tracking.urls')),  # Include your app's URLs here
]