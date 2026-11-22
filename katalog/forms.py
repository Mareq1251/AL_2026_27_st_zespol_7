from django import forms

from .models import Rezerwacja


class RezerwacjaForm(forms.ModelForm):
    class Meta:
        model = Rezerwacja
        fields = ["poczatek", "koniec", "cel"]
        widgets = {
            "poczatek": forms.DateTimeInput(
                format="%Y-%m-%dT%H:%M",
                attrs={"type": "datetime-local"},
            ),
            "koniec": forms.DateTimeInput(
                format="%Y-%m-%dT%H:%M",
                attrs={"type": "datetime-local"},
            ),
            "cel": forms.Textarea(attrs={"rows": 3}),
        }

    def clean(self):
        cleaned = super().clean()
        poczatek = cleaned.get("poczatek")
        koniec = cleaned.get("koniec")

        if poczatek and koniec and poczatek < koniec:
            kolizja = Rezerwacja.objects.filter(
                zasob_id=self.instance.zasob_id,
                status__in=[
                    Rezerwacja.Status.OCZEKUJACA,
                    Rezerwacja.Status.ZATWIERDZONA,
                ],
                poczatek__lt=koniec,
                koniec__gt=poczatek,
            )

            if self.instance.pk:
                kolizja = kolizja.exclude(pk=self.instance.pk)

            if kolizja.exists():
                raise forms.ValidationError(
                    "Ten zasób jest już zarezerwowany "
                    "w wybranym terminie. Wybierz inne godziny."
                )

        return cleaned