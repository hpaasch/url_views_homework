from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse


def index_view(request):
    return HttpResponse("Welcome to the Big Happy Family! Read about the Poston, Jacobs, Paasch and Kesgen households.")


def poston_view(request):
    return HttpResponse("The Postons are very popular. Just ask them! They drink, fish, swim, talk, laugh and hug. "
                        "A lot.")


def poston_parents_view(request):
    return HttpResponse("Tony and Jennifer raised three fine children and now plan to retire to the beach.")


def poston_kids_view(request):
    return HttpResponse("Matthew, Jon and Sarah will change the world. As soon as they turn 30.")


def poston_kids_career_view(request):
    return HttpResponse("Sarah is in fashion. Jon works in the woods. Matthew landscapes.")


def paasch_view(request):
    return HttpResponse("The Elaine Hope household is called TheLanding. Everyone hangs out here.")


def paasch_thelanding_view(request):
    return HttpResponse("At The Landing, everyone is welcome, as long as they bring S&P shakers.")


def paasch_activities_view(request):
    return HttpResponse("If you get tired of lake fun, you can always help build something. Like a deck.")


def paasch_latest_projects_view(request):
    return HttpResponse("Coming this fall: A small roof for the south wing of the deck.")


def jacobs_view(request):
    return HttpResponse("Richard and Gretchen hold down the South Carolina fort. They know EVERY movie.")


def jacobs_activities_view(request):
    return HttpResponse("Entertaining is a fine art in this home. Guests are welcomed and cared for.")


def kesgen_view(request):
    return HttpResponse("Annette's lovely mountain cabin is a wonderful respite.")

def kesgen_activities_view(request):
    return HttpResponse("Hiking. Hiking. Hiking. Hiking. Hiking. Hiking. Chocolate chip cookies.")
