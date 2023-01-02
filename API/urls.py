from django.urls import include, path
from .views import *

urlpatterns = [
    path('', Index.as_view()),
]