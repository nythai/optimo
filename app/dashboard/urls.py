from django.urls import path
from django.views.generic import RedirectView

from . import views

urlpatterns = [
    path('', RedirectView.as_view(pattern_name="dashboard:home", permanent=False), name="root"),
    path('home', views.dashboard_home, name="home"),
    path('search', views.dashboard_search, name="search")
]
