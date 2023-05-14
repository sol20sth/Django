from django.shortcuts import render


# Create your views here.
def throw(request):
    return render(request, "myapp/throw.html")


def catch(request):
    print(request.GET["message"])
    context = {"message": request.GET["message"], "key": request.GET.get("key")}
    return render(request, "myapp/catch.html", context)


def cal(request):
    return render(request, "myapp/cal.html")


def res(request):
    num1 = int(request.GET.get("num1"))
    num2 = int(request.GET.get("num2"))

    if num2 != 0:
        div = num1 / num2
    else:
        div = "error"

    context = {
        "num1": num1,
        "num2": num2,
        "sub": num1 - num2,
        "mul": num1 * num2,
        "div": div,
    }

    return render(request, "myapp/res.html", context)
