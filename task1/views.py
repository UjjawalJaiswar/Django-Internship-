from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def url(request):
    return render (request,"index.html")

def task(request):
    return render(request,"task.html")