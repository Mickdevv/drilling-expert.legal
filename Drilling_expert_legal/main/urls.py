from django.urls import path
from . import views

urlpatterns = [
    path("", views.redirectToHomePage, name="redirectToHomePage"),
    #path("homePage/", views.homePage, name="homePage"),
    path("eLearning/", views.eLearning, name="eLearning"),
    path("Expert/", views.Expert, name="Expert"),
    path("Investigator/", views.Investigator, name="Investigator"),
    path("Mediator/", views.Mediator, name="Mediator"),
    path("Arbitrator/", views.Arbitrator, name="Arbitrator"),
    path("DCR_Course_Feedback/", views.DCR_Course_Feedback, name="DCR_Course_Feedback"),
    path("placeholder/", views.placeholder, name="placeholder"),
]
