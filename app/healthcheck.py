import os

from django.http import JsonResponse

def healthcheck(request):
    """App health check, return OK if the app is alive"""
    version = os.environ.get("GIT_HASH")
    hostname = os.environ.get("HOSTNAME")
    return JsonResponse({
        'version': version,
        'status': 'KO',
        'hostname': hostname
        },
        status=400
        )
