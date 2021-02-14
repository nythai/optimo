from django.http import HttpResponse


def search_package(request):
    """
    Searches for given phrase in fulltext search engine.

    :return: renders view with found results
    @author: Kamil Żuchowski (kamil@kzuchowskinss.pl).
    """
    return HttpResponse("NOT IMPLEMENTED YET")
