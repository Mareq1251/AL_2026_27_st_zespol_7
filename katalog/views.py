from django.contrib.auth.decorators import login_required
from django.db import IntegrityError, transaction
from django.shortcuts import get_object_or_404, redirect, render

from .forms import RezerwacjaForm
from .models import Rezerwacja, Zasob


@login_required
def lista_zasobow(request):
    zasoby = Zasob.objects.filter(aktywny=True).order_by("nazwa")
    return render(request, "katalog/zasoby.html", {"zasoby": zasoby})


@login_required
def nowa_rezerwacja(request, zasob_id):
    zasob = get_object_or_404(Zasob, pk=zasob_id, aktywny=True)
    rezerwacja = Rezerwacja(
        zasob=zasob,
        uzytkownik=request.user,
    )

    form = RezerwacjaForm(
        request.POST if request.method == "POST" else None,
        instance=rezerwacja,
    )

    if request.method == "POST" and form.is_valid():
        try:
            with transaction.atomic():
                form.save()
        except IntegrityError as error:
            diagnostyka = getattr(error.__cause__, "diag", None)
            nazwa = getattr(diagnostyka, "constraint_name", None)

            if nazwa != "rezerwacja_bez_kolizji":
                raise

            form.add_error(
                None,
                "Termin został właśnie zajęty przez inną rezerwację. "
                "Wybierz inne godziny.",
            )
        else:
            return redirect("moje_rezerwacje")

    return render(
        request,
        "katalog/rezerwacja_form.html",
        {"form": form, "zasob": zasob},
    )


@login_required
def moje_rezerwacje(request):
    rezerwacje = (
        Rezerwacja.objects
        .filter(uzytkownik=request.user)
        .select_related("zasob")
    )
    return render(
        request,
        "katalog/moje_rezerwacje.html",
        {"rezerwacje": rezerwacje},
    )