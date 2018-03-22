from django.shortcuts import render

# Create your views here.


def guideline(request):
    return render(request, 'guideline.html')


def apply_mentoring(request):
    return render(request, 'apply_form.html')