from django import forms

class NameForm(forms.Form):
	your_name = forms.CharField(label='お名前', max_length=30)
