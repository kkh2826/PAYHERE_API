from django.urls import path, include
from .views import *

urlpatterns = [
    path('financeLedger/', FinanceLedger.as_view()),
    path('financeLedger/detail/<int:pk>/', FinanceLedgerDetail.as_view())
]