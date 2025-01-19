
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('sections.urls')),  # Подключаем URL-адреса приложения
]