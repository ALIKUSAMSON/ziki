from django import forms

class LoginForm(forms.Form):
	username = forms.CharField(max_length=50)
	password = forms.CharField(max_length=50, widget=forms.PasswordInput())

class SignUpForm(forms.Form):
	username = forms.CharField(max_length=50)
	email = forms.EmailField(max_length=254)
	password = forms.CharField(max_length=50, widget=forms.PasswordInput())
	confirm = forms.CharField(max_length=50, widget=forms.PasswordInput())