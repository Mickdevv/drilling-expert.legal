from django.urls import path
from . import views

urlpatterns = [
    path("", views.homePage, name="homePage"),
    path("homePage/", views.homePage, name="homePage"),
    path("eLearning/", views.eLearning, name="eLearning"),
    path("Expert/", views.Expert, name="Expert"),
    path("Investigator/", views.Investigator, name="Investigator"),
    path("Mediator/", views.Mediator, name="Mediator"),
    path("Arbitrator/", views.Arbitrator, name="Arbitrator"),
]
