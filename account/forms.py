from django import forms
from django.contrib.auth.forms import (
    AuthenticationForm,
    PasswordResetForm,
    SetPasswordForm,
)

from .models import Address, Customer


class UserAddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ["full_name", "phone", "address_line", "address_line2", "town_city", "postcode"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["full_name"].widget.attrs.update(
            {"class": "form-control mb-2 account-form", "placeholder": "Nome Completo"}
        )
        self.fields["phone"].widget.attrs.update({"class": "form-control mb-2 account-form", "placeholder": "+55"})
        self.fields["address_line"].widget.attrs.update(
            {"class": "form-control mb-2 account-form", "placeholder": "Endereço 1"}
        )
        self.fields["address_line2"].widget.attrs.update(
            {"class": "form-control mb-2 account-form", "placeholder": "Endereço 2"}
        )
        self.fields["town_city"].widget.attrs.update(
            {"class": "form-control mb-2 account-form", "placeholder": "Cidade"}
        )
        self.fields["postcode"].widget.attrs.update(
            {"class": "form-control mb-2 account-form", "placeholder": "Codigo Postal"}
        )


class UserLoginForm(AuthenticationForm):

    username = forms.CharField(
        label="Email/Usuário",
        widget=forms.TextInput(
            attrs={"class": "form-control mb-3", "placeholder": "Email/Usuário", "id": "login-username"}
        ),
    )
    password = forms.CharField(
        label="Senha",
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "Senha",
                "id": "login-pwd",
            }
        ),
    )


class RegistrationForm(forms.ModelForm):

    user_name = forms.CharField(label="Nome de usuário", min_length=4, max_length=50, help_text="Required")
    email = forms.EmailField(
        max_length=100, help_text="Required", error_messages={"required": "Desculpe, você vai precisar de um e-mail"}
    )
    password = forms.CharField(label="Senha", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repita sua senha", widget=forms.PasswordInput)

    class Meta:
        model = Customer
        fields = (
            "user_name",
            "email",
        )

    def clean_username(self):
        user_name = self.cleaned_data["user_name"].lower()
        r = Customer.objects.filter(user_name=user_name)
        if r.count():
            raise forms.ValidationError("O nome de usuário já existe")
        return user_name

    def clean_password2(self):
        cd = self.cleaned_data
        if cd["password"] != cd["password2"]:
            raise forms.ValidationError("As senhas não coincidem.")
        return cd["password2"]

    def clean_email(self):
        email = self.cleaned_data["email"]
        if Customer.objects.filter(email=email).exists():
            raise forms.ValidationError("Por favor, use outro e-mail, que já está sendo usado.")
        return email

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["user_name"].widget.attrs.update({"class": "form-control mb-3", "placeholder": "Username"})
        self.fields["email"].widget.attrs.update(
            {"class": "form-control mb-3", "placeholder": "E-mail", "name": "email", "id": "id_email"}
        )
        self.fields["password"].widget.attrs.update({"class": "form-control mb-3", "placeholder": "Senha"})
        self.fields["password2"].widget.attrs.update({"class": "form-control", "placeholder": "Repita sua senha"})


class PwdResetForm(PasswordResetForm):

    email = forms.EmailField(
        max_length=254,
        widget=forms.TextInput(attrs={"class": "form-control mb-3", "placeholder": "Email", "id": "form-email"}),
    )

    def clean_email(self):
        email = self.cleaned_data["email"]
        u = Customer.objects.filter(email=email)
        if not u:
            raise forms.ValidationError("Infelizmente não conseguimos encontrar esse endereço de e-mail.")
        return email


class PwdResetConfirmForm(SetPasswordForm):
    new_password1 = forms.CharField(
        label="New password",
        widget=forms.PasswordInput(
            attrs={"class": "form-control mb-3", "placeholder": "Nova Senha", "id": "form-newpass"}
        ),
    )
    new_password2 = forms.CharField(
        label="Repeat password",
        widget=forms.PasswordInput(
            attrs={"class": "form-control mb-3", "placeholder": "Nova Senha", "id": "form-new-pass2"}
        ),
    )


class UserEditForm(forms.ModelForm):

    email = forms.EmailField(
        label="E-mail da conta (não pode ser alterado)",
        max_length=200,
        widget=forms.TextInput(
            attrs={"class": "form-control mb-3", "placeholder": "email", "id": "form-email", "readonly": "readonly"}
        ),
    )

    user_name = forms.CharField(
        label="Nome",
        min_length=4,
        max_length=50,
        widget=forms.TextInput(
            attrs={
                "class": "form-control mb-3",
                "placeholder": "Seu nome",
                "id": "form-firstname",
                "readonly": "readonly",
            }
        ),
    )

    first_name = forms.CharField(
        label="Usuário",
        min_length=4,
        max_length=50,
        widget=forms.TextInput(
            attrs={"class": "form-control mb-3", "placeholder": "Nome de usuário", "id": "form-lastname"}
        ),
    )

    class Meta:
        model = Customer
        fields = (
            "email",
            "user_name",
            "first_name",
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["user_name"].required = True
        self.fields["email"].required = True
