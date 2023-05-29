from django.contrib import admin
from django.urls import path
from .views import Pricings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Pricings.as_view())
]
