from django import forms
from .models import PruebaDiagnostica

class PruebaDiagnosticaForm(forms.ModelForm):
    class Meta:
        model = PruebaDiagnostica
        fields = []