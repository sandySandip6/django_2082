from django.urls import path
from . import views

urlpatterns = [
    path("", views.polls_index, name="polls_index"),
    
    path("<int:qns_id>/", views.detail, name="detail"),
    
    path("<int:qns_id>/results/", views.result, name="result"),
    
    path("<int:qns_id>/vote/", views.vote, name="vote")
    
]