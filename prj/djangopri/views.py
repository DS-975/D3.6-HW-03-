from django.shortcuts import render


def index(reduest):
    return render(reduest, 'index.html')

