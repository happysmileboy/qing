from django.shortcuts import render, get_object_or_404
from accounts.models import Mentor_univ
# Create your views here.


def guideline(request, pk):
    mentor =get_object_or_404(Mentor_univ, pk=pk)
    ctx = {
        'mentor': mentor,
    }
    return render(request, 'guideline.html', ctx)


def apply_mentoring(request, pk):
    mentor = get_object_or_404(Mentor_univ, pk=pk)
    ctx={
        'mentor':mentor,
    }
    return render(request, 'apply_form.html',ctx)


def mentoring_reserved(request, pk):
    mentor = get_object_or_404(Mentor_univ, pk=pk)
    ctx = {
        'mentor': mentor,
    }
    return render(request, 'reserved_page.html',ctx)