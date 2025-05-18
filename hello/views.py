from django.http import HttpResponse
import os
from django.shortcuts import render

ENV = os.environ.get('ENV', 'dev-test')


def hello_world(request):
    return HttpResponse(f"<h1>Hello, django app!</h1><p>Środowisko: {ENV}</p><p>Made by: <b>Karolina Szymaszkiewicz - webszyk</b></p>")
