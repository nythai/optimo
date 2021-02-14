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
    if not search_phrase:
        messages.warning(request, "Provide searching phrase..")
    else:
        search_results = FullTextSearchService.search_package(search_phrase)

    return render(request, "dashboard/search.html", {"search_results": search_results})
