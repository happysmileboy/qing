import csv
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'qing.settings.prod')
import django
django.setup()

from accounts.models import *


f = open('Univ_category.csv', 'r')

for line in f.readlines()[1:]:
    l = line.split(',')
    id = l[0]
    univ = l[1]
    cat = l[2]
    dep = l[3]
    col = l[4]


    if not University.objects.filter(name=univ).exists():
        univ_obj = University.objects.create(name=univ)
    else:
        univ_obj = University.objects.get(name=univ)

    if not Categorized.objects.filter(university=univ_obj).filter(name=cat).exists():
        cat_obj = Categorized.objects.create(name=cat, university=univ_obj)
    else:
        cat_obj = Categorized.objects.get(university=univ_obj.pk, name=cat)

    if not Department.objects.filter(categorized=cat_obj, name=dep).exists():
        dep_obj = Department.objects.create(name=dep, categorized=cat_obj)
