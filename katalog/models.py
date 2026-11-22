from django.conf import settings
from django.contrib.postgres.constraints import ExclusionConstraint
from django.contrib.postgres.fields import (
    DateTimeRangeField,
    RangeBoundary,
    RangeOperators,
)
from django.core.exceptions import ValidationError
from django.db import models
from django.db.models import F, Q
from django.utils import timezone


class Zasob(models.Model):
    class Typ(models.TextChoices):
        SALA = "SALA", "Sala"
        SPRZET = "SPRZET", "Sprzęt"

    nazwa = models.CharField(max_length=150)
    typ = models.CharField(max_length=10, choices=Typ.choices)
    lokalizacja = models.CharField(max_length=200)
    opis = models.TextField(blank=True)
    aktywny = models.BooleanField(default=True)

    class Meta:
        verbose_name = "zasób"
        verbose_name_plural = "zasoby"

    def __str__(self):
        return self.nazwa


class Rezerwacja(models.Model):
    class Status(models.TextChoices):
        OCZEKUJACA = "OCZEKUJACA", "Oczekująca"
        ZATWIERDZONA = "ZATWIERDZONA", "Zatwierdzona"
        ODRZUCONA = "ODRZUCONA", "Odrzucona"
        ANULOWANA = "ANULOWANA", "Anulowana"

    uzytkownik = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        related_name="rezerwacje",
        verbose_name="użytkownik",
    )
    zasob = models.ForeignKey(
        Zasob,
        on_delete=models.PROTECT,
        related_name="rezerwacje",
        verbose_name="zasób",
    )
    poczatek = models.DateTimeField("początek")
    koniec = models.DateTimeField("koniec")
    cel = models.TextField("cel wykorzystania", max_length=1000)
    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.OCZEKUJACA,
    )
    utworzono = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "rezerwacja"
        verbose_name_plural = "rezerwacje"
        ordering = ["-poczatek"]
        constraints = [
            models.CheckConstraint(
                condition=Q(poczatek__lt=F("koniec")),
                name="rezerwacja_poprawny_termin",
                violation_error_message=(
                    "Koniec rezerwacji musi być późniejszy od początku."
                ),
            ),
            models.CheckConstraint(
                condition=Q(
                    status__in=[
                        "OCZEKUJACA",
                        "ZATWIERDZONA",
                        "ODRZUCONA",
                        "ANULOWANA",
                    ]
                ),
                name="rezerwacja_poprawny_status",
            ),
            ExclusionConstraint(
                name="rezerwacja_bez_kolizji",
                expressions=[
                    ("zasob", RangeOperators.EQUAL),
                    (
                        models.Func(
                            "poczatek",
                            "koniec",
                            RangeBoundary(),
                            function="TSTZRANGE",
                            output_field=DateTimeRangeField(),
                        ),
                        RangeOperators.OVERLAPS,
                    ),
                ],
                condition=Q(
                    status__in=["OCZEKUJACA", "ZATWIERDZONA"]
                ),
                violation_error_message=(
                    "Ten zasób jest już zarezerwowany w wybranym terminie."
                ),
            ),
        ]

    def clean(self):
        super().clean()
        errors = {}

        if self.poczatek and self.koniec:
            if self.poczatek >= self.koniec:
                errors["koniec"] = (
                    "Koniec musi być późniejszy od początku."
                )

        if self._state.adding and self.poczatek:
            if self.poczatek < timezone.now():
                errors["poczatek"] = (
                    "Rezerwacja nie może rozpoczynać się w przeszłości."
                )

        if self.zasob_id and not self.zasob.aktywny:
            errors["zasob"] = "Wybrany zasób jest nieaktywny."

        if errors:
            raise ValidationError(errors)

    def __str__(self):
        return f"{self.zasob} — {self.poczatek:%d.%m.%Y %H:%M}"