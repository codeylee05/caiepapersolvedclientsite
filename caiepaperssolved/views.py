from django.shortcuts import render
from django.http import HttpResponse


def index(request):

    return render(request, "caiepaperssolved/index.html")


def past_papers(request):

    return render(request, "caiepaperssolved/pastpapers.html")


def videos(request):

    return render(request, "caiepaperssolved/videos.html")


def about(request):

    return render(request, "caiepaperssolved/about.html")


def contact(request):

    return render(request, "caiepaperssolved/contact.html")


def store(request):

    return render(request, "caiepaperssolved/store.html")
