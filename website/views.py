from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

# Create your views here.
def index_view(request):
    return render(request, "website/index.html")

def about_view(request):
    return render(request, "website/about.html")

def contact_view(request):
    return render(request, 'website/Contact.html')