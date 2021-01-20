from django.shortcuts import render
from django.view.generic.list import ListView
from django.view.generic.detail import DetailView
from.models import Thread


# Create your views here.
class ThreadList(ListView):
	model: Thread

	def get_queryset(self):

class ThreadDetail(DetailView):
	model: Thread