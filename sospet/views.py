from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect 
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Pet

def login_user(request):
    return render(request, 'login.html')


@csrf_protect
def login_submit(request):
    if request.POST:
        usuario = request.POST.get('usuario')
        senha = request.POST.get('senha')
        user = authenticate(username=usuario, password=senha)

        if user is not None:
            login(request, user)
            return redirect('index')

        else:
            messages.error(request, 'Usuário ou senha inválidos, tente novamente!')

    return redirect('login')


@login_required(login_url='/login')
def index(request):
    return render(request, 'index.html')


def logout_user(request):
    logout(request)
    return redirect('login')


@login_required(login_url='/login')
def list_all_pets(request):

    pets = Pet.objects.filter(ativo=True)
    return render(request, 'list.html', {'pets': pets})


def list_user_pets(request):
    pet = Pet.objects.filter(ativo=True, usuario=request.user)
    return render(request, 'list.html', {'pets':pet})


def pet_detalhes(request, id):
    pet = Pet.objects.get(ativo=True, id=id)
    print(str(request.user)+' '+ str(pet.usuario))

    return render(request, 'pet.html', {'pet':pet})


@login_required(login_url='/login')
def registro_pet(request):
    return render(request, 'registro_pet.html')


@login_required(login_url='/login')
def set_pet(request):
    usuario = request.user
    nome = request.POST.get('nome')
    idade = request.POST.get('idade')
    cidade = request.POST.get('cidade')
    email = request.POST.get('email')
    telefone = request.POST.get('telefone')
    descricao = request.POST.get('descricao')
    foto = request.FILES.get('foto')
    user = request.user
    pet = Pet.objects.create(nome=nome, idade=idade, cidade=cidade, descricao=descricao, telefone=telefone, email=email, photo=foto, usuario=usuario)
    url = 'pet/detalhes/{}/'.format(pet.id)
    return redirect('index')

@login_required(login_url='/login')
def delete_pet(request, id):
    pet = Pet.objects.get(id=id)
    if pet.usuario == request.user:
        pet.delete()
    return redirect('index')

@login_required(login_url='/login')
def editar(request, id):
    pass