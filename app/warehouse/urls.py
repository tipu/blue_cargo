from django.urls import path

from .views import home, availability

urlpatterns = [
    path('', home, name='home'),
    path('/api/availability', availability, name='availability')
]
