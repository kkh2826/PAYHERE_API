from django.urls import include, path
from .views import *

urlpatterns = [
    path('account/', include('ACCOUNT.urls')),
]