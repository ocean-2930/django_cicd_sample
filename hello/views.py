# from django.shortcuts import render
from django.http import JsonResponse
import os, socket, datetime

def index(request):
    return JsonResponse({
        "message": "hello from github actions cicd",
        "host": socket.gethostname(),
        "deployed_at_env": os.environ.get("DEPLOYED_AT", "unknown"),
        "server_time": datetime.datetime.now().isoformat(),
        "message": "수정 확인2"
    })