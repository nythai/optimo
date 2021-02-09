from django.urls import path
from django.views.generic import RedirectView

from . import views

urlpatterns = [
    path('search', views.search_package, name="search-package")
]
