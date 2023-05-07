from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from .models import Company, Training, Profile, ProfileToCompanies
from .forms import UserForm, UserLoginForm
from django.core.files.storage import FileSystemStorage


def index(request):
    companies = Company.objects.all()
    return render(request, 'index.html', {'companies': companies})

#request.GET.get()
#kwargs['id']


def company(request, id):
    company = Company.objects.get(id=id)
    listTrainings = Training.objects.filter(idFKCompany=company)
    return render(request, 'company.html', {'company': company, 'listTrainings': listTrainings})


def create(request, id):
    if request.method == "POST":
        training = Training()
        company = Company.objects.get(id=id)
        training.name = request.POST.get("name")
        training.direction = request.POST.get("direction")
        training.date = request.POST.get("date")
        if request.POST.get("exp") == "on":
            training.exp = True
        else:
            training.exp = False
        if request.POST.get("educ") == "on":
            training.educ = True
        else:
            training.educ = False

        training.idFKCompany = company
        training.save()
        return HttpResponse("Гуд")


def update_user_data(user):
    Profile.objects.update_or_create(user=user, profilePic=user.profilePic)


def registration(request):
    if request.method == "POST" and request.FILES:
        form = UserForm(request.POST)
        prof = ProfileToCompanies()
        if form.is_valid():
            file = request.FILES['profilePic']
            user = form.save()
            user.refresh_from_db()
            user.profilePic = file
            user.save()

            update_user_data(user)

            companies_ids = request.POST.getlist("companies")
            companies = Company.objects.filter(id__in=companies_ids)
            profileCheck = Profile.objects.get(user=user)
            profileCheck.proftocomp.set(companies)
            login(request, user)
            return HttpResponse("ГУДЕС")
        else:
            return HttpResponse("не туда")
    else:
        form = UserForm()
        companies = Company.objects.all()
        return render(request, 'register.html', {'form': form, 'companies': companies})


def auth(request):
    if request.method == "POST":
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            login(request, user)
            return HttpResponse("Успешно вошел")
    else:
        form = UserLoginForm()
        return render(request, 'auth.html', {'form': form})


def profile(request):
    prof = Profile.objects.get(user=request.user)
    profPic = prof.profilePic
    return render(request, 'profile.html', {'profPic': profPic})


def close_log(request):
    logout(request)
    return HttpResponse("Вышел из аккаунта")