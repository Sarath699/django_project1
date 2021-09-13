from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
# Create your views here.

def logout(request):
	auth.logout(request)
	messages.info(request, "Succesfully Logged out!!!")
	return redirect('login')

def login(request):
	if request.method == "POST":
		username = request.POST['username']
		password = request.POST['password']
		user = auth.authenticate(username=username, password=password)
		if user is not None:
			auth.login(request, user)
			messages.info(request, "Succesfully Logged in")
			return redirect("/")
		else:
			messages.error(request, "Invalid UserName Or PassWord")
			return redirect("login")
	else:
		return render(request, 'login_page.html')


def register(request):
	if request.method == "POST":
		first_name = request.POST["first_name"]
		last_name = request.POST["last_name"]
		email = request.POST['email']
		password1 = request.POST['password1']
		password2 = request.POST['password2']
		username = request.POST['username']
		if password1 != password2:
			messages.error(request, "PassWord Mismatch")
			return redirect("register")
		elif User.objects.filter(username=username).exists():
			messages.info(request, "username already exists")
			return redirect("register")
		elif User.objects.filter(email=email).exists():
			messages.info(request, "email already exists in data base")
			return redirect("register")
		else:
			user = User.objects.create_user(username=username, email=email, first_name=first_name, last_name=last_name, password=password1)
			user.save()
			messages.success(request, "User Succesfully Created")
			return redirect("login")
	else:
		return render(request, 'register.html')