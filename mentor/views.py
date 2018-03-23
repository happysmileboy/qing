from django.shortcuts import render, get_object_or_404

from accounts.models import Mentor_univ
# Create your views here.


def consult_main(request):
    return render(request, 'consult_main.html')


def search_univ_mentor(request):
    mentors = Mentor_univ.objects.all()

    ctx ={
        'mentors':mentors,
    }
    return render(request, 'search_univ_mentor.html', ctx)


def mentor_profile(request, username):
    ctx = {
        'mentor': get_object_or_404(
            Mentor_univ, user__username=username
        )
    }
    return render(request, 'mentor_profile.html',ctx)


def mentor_profile2(request, username):
    ctx = {
        'mentor': get_object_or_404(
            Mentor_univ, user__username=username
        )
    }
    return render(request, 'mentor_profile2.html',ctx)