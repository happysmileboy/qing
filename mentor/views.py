from django.shortcuts import render

# Create your views here.

def consult_main(request):
    return render(request, 'consult_main.html')