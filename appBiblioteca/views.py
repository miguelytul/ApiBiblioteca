from django.shortcuts import render, redirect
# render -> abre/renderiza páginas HTML
# redirect -> redireciona para outra rota

from .models import Usuario
# Importa o model Usuario do arquivo models.py


# Função responsável pelo cadastro de usuários
def cadastro(request):

    # Verifica se o formulário foi enviado usando POST
    if request.method == "POST":

        # Pega os dados enviados pelo formulário HTML
        nome = request.POST.get("nome")
        email = request.POST.get("email")
        senha = request.POST.get("senha")

        # Cria um novo usuário no banco de dados
        Usuario.objects.create(
            nome=nome,
            email=email,
            senha=senha
        )

        # Redireciona novamente para a página de cadastro
        return redirect("cadastro")

    # Se não for POST, apenas abre a página cadastro.html
    return render(request, 'usuarios/cadastro.html')