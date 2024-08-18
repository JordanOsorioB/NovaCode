from django import forms
from .models import Contacto

class ContactoForm(forms.ModelForm):
    class Meta:
        model = Contacto
        fields = ['nombre_contacto', 'apellidos_contacto', 'email', 'telefono', 'mensaje']
        widgets = {
            'nombre_contacto': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese su nombre'}),
            'apellidos_contacto': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese sus apellidos'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese su correo electrónico'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese su número de teléfono'}),
            'mensaje': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Ingrese su mensaje', 'rows': 3}),
        }

    def clean(self):
        cleaned_data = super().clean()
        nombre = cleaned_data.get('nombre_contacto')
        apellidos = cleaned_data.get('apellidos_contacto')
        email = cleaned_data.get('email')
        telefono = cleaned_data.get('telefono')

        if not nombre:
            self.add_error('nombre_contacto', 'Este campo es obligatorio.')
        if not apellidos:
            self.add_error('apellidos_contacto', 'Este campo es obligatorio.')
        if not email:
            self.add_error('email', 'Este campo es obligatorio.')
        if not telefono:
            self.add_error('telefono', 'Este campo es obligatorio.')

        return cleaned_data
