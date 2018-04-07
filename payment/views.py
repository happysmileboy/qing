from django.shortcuts import render, get_object_or_404, redirect
from accounts.models import User, Mentor_univ
from .forms import ReservationForm
from .models import Reservation
from django.http import HttpResponse, Http404, JsonResponse
# Create your views here.


def guideline(request, pk):
    mentor =get_object_or_404(Mentor_univ, pk=pk)
    ctx = {
        'mentor': mentor,
    }
    return render(request, 'guideline.html', ctx)


def apply_mentoring(request, pk):
    mentor = get_object_or_404(Mentor_univ, pk=pk)
    form = ReservationForm(request.POST or None)
    if request.method == 'POST':
        reservation =form.save(commit=False)
        reservation.mentor = mentor
        reservation.user = request.user
        reservation.save()
        return redirect(reservation.get_absolute_url())

    ctx={
            'mentor' : mentor,
            'form':form,
        }
    return render(request, 'apply_form.html',ctx)


def mentoring_reserved(request, pk):
    reservation = get_object_or_404(Reservation, pk=pk, user=request.user)
    mentor = reservation.mentor
    ctx = {
        'mentor':mentor,
        'reservation': reservation,
    }

    return render(request, 'reserved_page.html',ctx)



def my_reservation(request, username):
    user = get_object_or_404(User, username=username)
    if get_object_or_404(Mentor_univ, user=request.user) :
        mentor = get_object_or_404(Mentor_univ, user=request.user)
        reservation = Reservation.objects.filter(mentor=mentor)
        ctx = {
            'reservation': reservation,
        }
        return render(request, 'mypage.html', ctx)
    else:
        return render(request, 'mypage.html')

