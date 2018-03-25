from django.shortcuts import render


def main(request):
    return render(request, 'main.html')


def service(request):
    return render(request, 'service.html')