from django.shortcuts import render
from django.http import JsonResponse

from django.views.decorators.csrf import ensure_csrf_cookie

@ensure_csrf_cookie
def token_security(request):
    return JsonResponse("CSRF Retrived", safe=False)

# Create your views here.
