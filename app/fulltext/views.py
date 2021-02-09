from django.http import HttpResponse


def search_package(request):
    """
    Searches for given phrase in fulltext search engine.

    :return: renders view with found results
    """
    return HttpResponse("NOT IMPLEMENTED YET")
