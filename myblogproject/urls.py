from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('myblog/', include('myblogapp.urls')),
    path('admin/', admin.site.urls),
]
