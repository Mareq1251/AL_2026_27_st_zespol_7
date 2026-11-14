from django.shortcuts import render

# Create your views here.
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from .models import Zasob


@login_required
def lista_zasobow(request):
    zasoby = Zasob.objects.filter(aktywny=True).order_by("nazwa")
    return render(request, "katalog/zasoby.html", {"zasoby": zasoby})