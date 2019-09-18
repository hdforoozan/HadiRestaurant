from django import forms

class SearchForm(forms.Form):
    search_food = forms.CharField(max_length=200)
