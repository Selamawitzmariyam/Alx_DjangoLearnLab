
from django.contrib import admin
from django.urls import path, include  # Include is necessary to reference app URLs

urlpatterns = [
    path('admin/', admin.site.urls),
    path('relationship/', include('relationship_app.urls')),  # Include the app's URLs
]
