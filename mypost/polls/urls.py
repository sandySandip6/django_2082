from django.urls import path
from . import views

app_name = "polls"

urlpatterns = [
    path("", views.polls_index, name="polls_index"),
    
    path("<int:qns_id>/details/", views.details, name="details"),
    
    path("<int:qns_id>/results/", views.results, name="results"),
    
    path("<int:qns_id>/vote/", views.vote, name="vote")
    
]