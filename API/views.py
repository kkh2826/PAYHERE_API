from rest_framework.views import APIView
from django.http import JsonResponse

# Create your views here.
class Index(APIView):
    def get(self, request):
        return JsonResponse()