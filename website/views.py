from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

# Create your views here.
def index_view(request):
    return HttpResponse("<h1>Index</h1>")

def about_view(request):
    return HttpResponse("<h1>About</h1>")

def contact_view(request):
    return HttpResponse("<h1>Contact</h1>")