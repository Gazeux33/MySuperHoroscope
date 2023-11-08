from django.shortcuts import render,redirect
from django.contrib.auth import get_user_model,login,logout,authenticate
from django.contrib import messages
import re


User = get_user_model()

def is_valid_email(email):
    pattern = re.compile(r'^[\w\.-]+@[\w\.-]+\.\w+$')
    return bool(pattern.match(email))

def username_not_same_as_password(username, password):
    return username != password

def signup(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        email = request.POST.get("email")

        if User.objects.filter(username=username).exists():
            messages.error(request, "Ce nom d'utilisateur existe déjà.")
        elif not is_valid_email(email):
            messages.error(request, "L'adresse e-mail n'est pas valide.")
        elif not username_not_same_as_password(username, password):
            messages.error(request, "Le nom d'utilisateur et le mot de passe ne doivent pas être identiques.")
        else:
            user = User.objects.create_user(username=username, password=password, email=email)
            login(request, user)
            return redirect('index')

    return render(request, 'signup.html')

def login_user(request):
    if request.method == "POST":
        password = request.POST.get("password")
        email = request.POST.get("email")

        try:
            user_obj = User.objects.get(email=email)
            user = authenticate(request, username=user_obj.username, password=password)
            if user:
                login(request, user)
                return redirect('index')
            else:
                messages.error(request, "Mot de passe incorrect.")
        except User.DoesNotExist:
            messages.error(request, "Adresse e-mail incorrecte.")

    return render(request, 'login.html')      

def logout_user(request):
    logout(request)
    return redirect('index')

