from django.shortcuts import render, redirect, get_object_or_404
from .forms import CandiForm, Login, Registration
from django.contrib.auth import authenticate, login, logout
from .filters import CandiFilter
from .models import Candidate


def index(request):
    return redirect("hummly:login")


def candi_add(request):
    form = CandiForm(request.POST or None, request.GET or None)
    if form.is_valid() and request.POST:
        newcandi = form.save(commit=False)
        newcandi.save()
        return redirect("cian:index")
    return render(request, 'cian/simple_form.html', {"form": form})


def candi_search(request):
    print(request.GET['skills'])
    form = CandiForm(request.POST or None, request.GET or None)

    if form.is_valid():
        fields = ['Serial No', 'Candidate Name', 'Email', 'Mobile No', 'Current Location', 'Nearest City',
         'ug_course', 'ug_institute_name', 'ug_tier_one', 'ug_passing_year', 'pg_course', 'pg_institute_name',
         'pg_tier_one', 'pg_passing_year', 'Preferred Location', 'Resume', 'Work Experience', 'Analytics Experience',
         'Current Employer', 'CTC', 'Current Designation', 'Skills', 'any_other_course']
        candi = Candidate.objects.all()
        result = CandiFilter(request.GET, queryset=candi)
        return render(request, 'cian/result.html', {"result": result, "heads": fields})
    return render(request, 'cian/search.html', {"form": form})


def gen_form(request):
    form = CandiForm(request.POST or None, request.GET or None)
    if form.is_valid() and request.GET:
        fields = ['Serial No', 'Candidate Name', 'Email', 'Mobile No', 'Current Location', 'Nearest City',
         'ug_course', 'ug_institute_name', 'ug_tier_one', 'ug_passing_year', 'pg_course', 'pg_institute_name',
         'pg_tier_one', 'pg_passing_year', 'Preferred Location', 'Resume', 'Work Experience', 'Analytics Experience',
         'Current Employer', 'CTC', 'Current Designation', 'Skills', 'any_other_course']
        candi = Candidate.objects.all()
        result = CandiFilter(request.GET, queryset=candi)
        return render(request, 'cian/result.html', {"result": result, "heads": fields})
    if form.is_valid() and request.POST:
        newcandi = form.save(commit=False)
        newcandi.save()
        return redirect("cian:index")
    return render(request, 'cian/simple_form.html', {"form": form})


def user_login(request):
    form = Login(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(username=username, password=password)
        if user is not None and user.is_active:
            login(request, user)
            return redirect('hummly:form')

    return render(request, 'cian/login.html', {'form': form})


def user_logout(request):
    logout(request)
    return redirect('cian:login')


def user_registration(request):
    form = Registration(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        email = form.cleaned_data['email']
        user.set_password(password)
        user.save()
        user = authenticate(username=username, password=password)
        login(request, user)
        return redirect('cian:index')
    return render(request, 'cian/register.html', {'form': form})


