from django.http import JsonResponse
import os

def healthcheck(request):
    """App health check, return OK is the app is alive"""
    version = os.environ.get("GIT_HASH")
    return JsonResponse({'version': version, 'status': 'OK'})
