from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    #return HttpResponse("Bienvenidos a mi landingpage")
    return render(request, "landingpage/index.html")
