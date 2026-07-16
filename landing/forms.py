from django import forms


class ContactForm(forms.Form):
    """Lead / contact form shown in the landing's contact section."""

    name = forms.CharField(
        label="Nombre y apellido",
        max_length=120,
        widget=forms.TextInput(attrs={"placeholder": "Su nombre", "autocomplete": "name"}),
    )
    email = forms.EmailField(
        label="Correo electrónico",
        widget=forms.EmailInput(attrs={"placeholder": "correo@empresa.com", "autocomplete": "email"}),
    )
    company = forms.CharField(
        label="Empresa",
        max_length=120,
        required=False,
        widget=forms.TextInput(attrs={"placeholder": "Nombre de su empresa"}),
    )
    phone = forms.CharField(
        label="Teléfono",
        max_length=40,
        required=False,
        widget=forms.TextInput(attrs={"placeholder": "+595 ...", "autocomplete": "tel"}),
    )
    message = forms.CharField(
        label="¿Cómo podemos ayudarle?",
        widget=forms.Textarea(attrs={"rows": 4, "placeholder": "Cuéntenos sobre su proyecto"}),
    )
    # Simple honeypot to deter bots — real users leave it empty.
    website = forms.CharField(required=False, widget=forms.HiddenInput)

    def is_spam(self) -> bool:
        return bool(self.cleaned_data.get("website"))
