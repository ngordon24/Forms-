from django import forms


class warmupTwoForm(forms.Form):
    repeatedtext = forms.CharField()
    timesrepeated = forms.IntegerField()


class logicTwoForm(forms.Form):
    numberone = forms.IntegerField()
    numbertwo = forms.IntegerField()
    numberthree = forms.IntegerField()


class stringTwoForm(forms.Form):
    text = forms.CharField()


class listTwoForm(forms.Form):
    numbers = forms.CharField()
