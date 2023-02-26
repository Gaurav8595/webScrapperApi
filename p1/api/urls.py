from django.urls import path
from .views import Web

urlpatterns = [
    path('', Web.as_view(),name="web"),
]
