from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


def Main_Page(request: HttpRequest) -> HttpResponse:
    return render(request, "Main_Page.html")
