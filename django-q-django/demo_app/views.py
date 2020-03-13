from time import sleep

# 3rd
from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse


def index(request):
    json_payload = {"message": "Hello World"}
    sleep(10)
    return JsonResponse(json_payload)
