from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from app.forms import AgeForm, HelloForm, OrderForm


# Create your views here.
def calc(request: HttpRequest):
    form = AgeForm(request.GET)
    if form.is_valid():
        X = form.cleaned_data["X"]
        Y = form.cleaned_data["Y"]
        answer = X - Y
        return render(
            request, "calc.html", {"form": form, "X": X, "Y": Y, "answer": answer}
        )
    else:
        return render(request, "calc.html", {"form": AgeForm()})


def hello(request: HttpRequest):
    form = HelloForm(request.GET)
    if form.is_valid():
        Name = form.cleaned_data["Name"]
        return render(request, "Hello.html", {"form": form, "Name": Name})
    else:
        return render(request, "Hello.html", {"form": form})


def order(request: HttpRequest):
    form = OrderForm(request.GET)
    if form.is_valid():
        Burgers = form.cleaned_data["Burgers"]
        Fries = form.cleaned_data["Fries"]
        Drinks = form.cleaned_data["Drinks"]

        total = Burgers * 4.50 + Fries * 1.5 + Drinks * 1

        return render(
            request,
            "Order.html",
            {"Burger": Burgers, "Fries": Fries, "Drinks": Drinks, "total": total},
        )
    else:
        return render(request, "Order.html", {"form": form})
