from django.contrib import messages
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from packages.services import FullTextSearchService


def dashboard_home(request):
    return render(request, "dashboard/home.html")


@csrf_exempt
def dashboard_search(request):
    search_phrase = request.GET.get("search_phrase")
    search_results = []
    if search_phrase is not None and len(search_phrase) == 0:
        messages.warning(request, "Provide searching phrase..")
    else:
        search_results = FullTextSearchService.search_package(search_phrase)
        if len(search_results) == 0:
            messages.warning(request, "Not found any results.")

    return render(request, "dashboard/search.html", {"packages": search_results})
