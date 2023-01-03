from django.urls import path, include
from .views import *

urlpatterns = [
    path('insertFinanceLedger/', FinanceLedger.as_view()),
]