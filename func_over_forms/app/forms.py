from django import forms


class heyForm(forms.Form):
    name = forms.CharField()


class ageInForm(forms.Form):
    birthyear = forms.IntegerField()
    endyear = forms.IntegerField()


class orderForm(forms.Form):
    burger = forms.IntegerField()
    fries = forms.IntegerField()
    drink = forms.IntegerField()
