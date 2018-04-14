from django.shortcuts import render, get_object_or_404

from accounts.models import Mentor_univ, Department
# Create your views here.


def consult_main(request):
    return render(request, 'consult_main.html')


def search_univ_mentor(request, department_pk=None):
    if department_pk is not None:
        mentors=Mentor_univ.objects.filter(univ_categories__pk=department_pk)
        try:
            departments = Department.objects.get(pk=department_pk)
        except Department.DoesNotExist:
            raise Http404('없는 학부입니다.')
        ctx ={
        'mentors':mentors,
        'departments':departments,
        }
    else:
        mentors= Mentor_univ.objects.all()
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