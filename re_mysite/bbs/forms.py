from django import forms

class NameForm(forms.form):
	your_name = forms.CharField(label='お名前', max_length=30)
