from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def view(request):
    return HttpResponse("<h1>Test</h1>")