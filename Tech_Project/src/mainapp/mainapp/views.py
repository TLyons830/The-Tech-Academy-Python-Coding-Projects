from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse


def index(request):
    return render(request, "index.html")


def CreateNewAccount(request):
    return render(request, "CreateNewAccount.html")


def AddTransaction(request):
    return render(request, "AddTransaction.html")


def BalanceSheet(request):
    return render(request, "BalanceSheet.html")