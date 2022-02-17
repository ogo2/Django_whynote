from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    current_user = request.user
    print(current_user.id)

    return render(request, 'chart/index.html')