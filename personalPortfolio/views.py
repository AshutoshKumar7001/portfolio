from django.shortcuts import render, HttpResponse
from django.template import loader
# Create your views here.
def Home(req):
    return render(req, "index.html")