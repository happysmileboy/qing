from django.shortcuts import render, redirect, render_to_response
from django.urls import reverse
from django.db import models
from .models import Notice


from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def notice_list(request):
    notice_list = Notice.objects.all().order_by('-id')
    page = request.GET.get('page', 1)

    paginator = Paginator(notice_list, 10)
    try:
        notices = paginator.page(page)

    except PageNotAnInteger:
        notices = paginator.page(1)
    except EmptyPage:
        notices = paginator.page(paginator.num_pages)

    return render(request, 'notice/notice_list.html', { 'notices': notices })




def notice_detail(request, pk):
    notice = Notice.objects.get(pk=pk)
    ctx = {
        'notice': notice
    }
    return render(request, 'notice/notice_detail.html', ctx)