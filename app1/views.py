from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
	return render(request, "base.html")

def addition(request):
	x=int(request.POST['num1'])
	y=int(request.POST['num2'])
	result=x+y
	return render(request, "result.html", {"result":result})