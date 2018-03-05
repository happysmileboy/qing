from django.shortcuts import render

# Create your views here.


def consult_main(request):
    return render(request, 'consult_main.html')


def search_univ_mentor(request):
    return render(request, 'search_univ_mentor.html')