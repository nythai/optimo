from django.shortcuts import render


def dashboard_home(request):
    return render(request, "dashboard/home.html")


def dashboard_search(request):
    return render(request, "dashboard/search.html")
