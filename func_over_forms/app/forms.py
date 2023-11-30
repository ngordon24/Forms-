from django import forms


class AgeForm(forms.Form):
    X = forms.IntegerField(required=True)
    Y = forms.IntegerField(required=True)


class HelloForm(forms.Form):
    Name = forms.CharField()


class OrderForm(forms.Form):
    Burgers = forms.IntegerField()
    Fries = forms.IntegerField()
    Drinks = forms.IntegerField()
