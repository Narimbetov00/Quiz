from django.shortcuts import render,HttpResponse
from .models import *
# Create your views here.


def SorawView(request):
    soraw = Questions.objects.all().values()
    answers = Answer.objects.all().values()
    return HttpResponse(soraw,answers)