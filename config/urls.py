from django.contrib import admin
from django.urls import path, include
from agenda import urls as agenda


urlpatterns = [
    path('admin/', admin.site.urls),
    path('agenda/', include(agenda))
]
