from django.contrib import admin
from django.urls import path, include # imported include


urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('', include('blog.urls')), # included blog urls
    path('admin/', admin.site.urls),
]
