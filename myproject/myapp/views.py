from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
     if request.method == "GET":
        return HttpResponse("Success", content_type="text/plain", status=200)
     else:
        return HttpResponse("error", content_type="text/plain", status=404)
         