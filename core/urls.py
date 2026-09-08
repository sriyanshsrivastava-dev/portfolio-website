from os import name

from django.urls import path
from core.views import CoreView

# all core paths goes here

urlpatterns = [
    path('', CoreView.as_view(), name='home'),
]