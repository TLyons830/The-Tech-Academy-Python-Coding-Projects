from django.shortcuts import render, redirect
from checkbook.forms import AccountInfo


def index(request):
    return render(request, "index.html")


def BalanceSheet(request):
    return render(request, "BalanceSheet.html")


def CreateNewAccount(request):
    form = AccountInfo(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('index')
    else:
        print(form.errors)
        form = AccountInfo()
    context = {
        'form': form,
    }
    return render(request, "CreateNewAccount.html", context)


def AddTransaction(request):
    return render(request, "AddTransaction.html")
