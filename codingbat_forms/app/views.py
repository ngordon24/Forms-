from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from app.forms import warmupTwoForm, logicTwoForm, stringTwoForm, listTwoForm

# Create your views here.


def warmupTwo(request):
    form = warmupTwoForm(request.GET)
    if form.is_valid():
        timesRepeated = form.cleaned_data["timesrepeated"]
        repeatedText = form.cleaned_data["repeatedtext"]

        frontLength = 3
        if frontLength > len(repeatedText):
            frontLength = len(repeatedText)
        front = repeatedText[:frontLength]

        result = ""
        for i in range(timesRepeated):
            result = result + front
        return render(
            request,
            "warmup.html",
            {
                "timesrepeated": timesRepeated,
                "repeatedtext    ": repeatedText,
                "result": result,
            },
        )
    else:
        return render(request, "warmup.html")


def logicTwo(request):
    form = logicTwoForm(request.GET)
    if form.is_valid():

        def removeTeens(number):
            if (
                number == 13
                or number == 14
                or number == 17
                or number == 18
                or number == 19
            ):
                return 0
            else:
                return number

        numberOne = removeTeens(form.cleaned_data["numberone"])
        numberTwo = removeTeens(form.cleaned_data["numbertwo"])
        numberThree = removeTeens(form.cleaned_data["numberthree"])
        result = numberOne + numberTwo + numberThree

        return render(request, "logic.html", {"result": result})

    else:
        return render(request, "logic.html")


def stringTwo(request):
    form = stringTwoForm(request.GET)
    if form.is_valid():
        text = form.cleaned_data["text"]
        for i in range(len(text) - 2):  # Adjust the range
            if text[i : i + 3] == "xyz" and (i == 0 or text[i - 1] != "."):
                result = True
                return render(request, "string.html", {"result": result})

        result = False
        return render(request, "string.html", {"result": result})
    else:
        result = ""
        return render(request, "string.html", {"result": result})


def listTwo(request):
    def centeredAverage(numbers):
        numbers = sorted(numbers)
        return sum(numbers[1:-1]) // (len(numbers) - 2)

    form = listTwoForm(request.GET)

    result = None

    if form.is_valid():
        numbers = form.cleaned_data["numbers"]
        numbers = list(map(int, numbers.split(",")))
        result = centeredAverage(numbers)

        return render(request, "list.html", {"result": result})

    else:
        return render(request, "list.html")
