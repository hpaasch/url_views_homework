from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse


def index_view(request):
    return HttpResponse("Welcome to the Big Happy Family! Read about the Poston, Jacobs, Paasch and Kesgen households.")
