from django.shortcuts import render
from django.http import HttpResponse
from HolaMundo.models import Author

# Create your views here.
def hola_mundo(request):
    return HttpResponse("<h1>Hola Mundo</h1>")

def home(request):
    authors = Author.objects.all()
    return render(request,"index.html", {'authors' : authors})
