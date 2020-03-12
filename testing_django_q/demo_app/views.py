from django.shortcuts import render
from django.http import JsonResponse
from time import sleep

# Create your views here.


def index(request):
    json_payload = {"message": "Hello World!"}
    sleep(10)
    return JsonResponse(json_payload)
