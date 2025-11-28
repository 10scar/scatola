from django import forms
from preguntas.models import TipoExamen, Componente
from rutas.models import Ruta


from django import forms
from .models import Ruta
from preguntas.models import TipoExamen, Componente

class RutaUsuarioForm(forms.ModelForm):
    examenes = forms.ModelMultipleChoiceField(
        queryset=TipoExamen.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=True,
    )
    componentes = forms.ModelMultipleChoiceField(
        queryset=Componente.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=True,
    )

    class Meta:
        model = Ruta
        fields = ["examenes", "componentes"]

    def clean(self):
        cleaned = super().clean()
        examenes = cleaned.get("examenes")
        componentes = cleaned.get("componentes")

        if not examenes or len(examenes) == 0:
            raise forms.ValidationError("Debes seleccionar al menos una ruta (ICFES o UNAL).")

        if not componentes or len(componentes) == 0:
            raise forms.ValidationError("Debes seleccionar al menos un componente.")

        allowed_comps = Componente.objects.filter(tipo_examen__in=examenes)
        disallowed = [c for c in componentes if c not in allowed_comps]

        if disallowed:
            nombres = ", ".join([str(d) for d in disallowed])
            raise forms.ValidationError(f"Los siguientes componentes no pertenecen a las rutas seleccionadas: {nombres}")

        for ex in examenes:
            comps_for_ex = [c for c in componentes if c.tipo_examen_id == ex.id]
            if len(comps_for_ex) == 0:
                raise forms.ValidationError(f"Si seleccionas '{ex.nombre}' debes elegir al menos un componente para esa ruta.")

        return cleaned