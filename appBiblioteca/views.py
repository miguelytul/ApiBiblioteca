from django.shortcuts import render, redirect
from .models import Usuario
# Create your views here.
def cadastro(request):
    if request.method == "POST":
        nome = request.POST.get("nome")
        email = request.POST.get("email")
        senha = request.POST.get("senha")

        Usuario.objects.create(
            nome = nome,
            email = email,
            senha = senha

        )
        return redirect("cadastro")


    return render(request, 'usuarios/cadastro.html')

