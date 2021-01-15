from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
	return HttpResponse("Vista Inicio")

def about(request):
	return HttpResponse("Vista Historia")