from django.shortcuts import render
from app.forms import heyForm, ageInForm, orderForm


def hey(request):
    form = heyForm(request.GET)
    if form.is_valid():
        name = (form.cleaned_data["name"]).upper()
        return render(request, "hey.html", {"name": name})
    else:
        return render(request, "hey.html")


def agein(request):
    form = ageInForm(request.GET)
    if form.is_valid():
        birthyear = form.cleaned_data["birthyear"]
        endyear = form.cleaned_data["endyear"]
        agein = endyear - birthyear
        return render(
            request,
            "agein.html",
            {"birthyear": birthyear, "endyear": endyear, "agein": agein},
        )
    else:
        return render(request, "agein.html")


def order(request):
    form = orderForm(request.GET)
    if form.is_valid():
        burger = form.cleaned_data["burger"] * 4.5
        fries = form.cleaned_data["fries"] * 1.5
        drink = form.cleaned_data["drink"]

        totalCost = burger + fries + drink

        return render(
            request,
            "order.html",
            {"burger": burger, "fries": fries, "drink": drink, "totalCost": totalCost},
        )
    else:
        return render(request, "order.html")
