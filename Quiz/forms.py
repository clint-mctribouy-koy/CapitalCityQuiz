from django import forms

class QuizForm(forms.Form):
    capital_city_field = forms.CharField(label='',max_length=100, required=True)
