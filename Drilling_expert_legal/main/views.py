from django.http import HttpResponse
from django.template import loader
from django.shortcuts import redirect


def redirectToHomePage(request):
    return redirect("/Arbitrator/")

# def homePage(request):
#     template = loader.get_template('homePage.html')
#     context = {}
#     return HttpResponse(template.render(context, request))

def Arbitrator(request):
    template = loader.get_template('Arbitrator.html')
    context = {}
    return HttpResponse(template.render(context, request))

def Mediator(request):
    template = loader.get_template('Mediator.html')
    context = {}
    return HttpResponse(template.render(context, request))

def Expert(request):
    template = loader.get_template('Expert.html')
    context = {}
    return HttpResponse(template.render(context, request))

def Investigator(request):
    template = loader.get_template('Investigator.html')
    context = {}
    return HttpResponse(template.render(context, request))

def eLearning(request):
    template = loader.get_template('eLearning.html')
    context = {}
    return HttpResponse(template.render(context, request))

def DCR_Course_Feedback(request):
    template = loader.get_template('DCR_Course_Feedback.html')
    context = {}
    return HttpResponse(template.render(context, request))

def placeholder(request):
    template = loader.get_template('placeholder.html')
    context = {}
    return HttpResponse(template.render(context, request))
