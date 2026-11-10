from datetime import date

from django.shortcuts import render


def index(request):
    return render(request, 'index.html', {'current_year': date.today().year})
