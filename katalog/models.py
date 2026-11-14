from django.db import models


class Zasob(models.Model):
    class Typ(models.TextChoices):
        SALA = "SALA", "Sala"
        SPRZET = "SPRZET", "Sprzęt"

    nazwa = models.CharField(max_length=150)
    typ = models.CharField(max_length=10, choices=Typ.choices)
    lokalizacja = models.CharField(max_length=200)
    opis = models.TextField(blank=True)
    aktywny = models.BooleanField(default=True)

    def __str__(self):
        return self.nazwa