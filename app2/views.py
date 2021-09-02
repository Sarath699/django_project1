from django.shortcuts import render
from django.http import HttpResponse
from .models import Travello
# Create your views here.

def travello(request):

	dests = Travello.objects.all()	
	return render(request, "dynamic_travello.html", {"travv": dests})
