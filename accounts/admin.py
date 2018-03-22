from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from .models import User, Mentor_univ, EmailConfirm, Categorized
# Register your models here.

admin.site.register(User)
admin.site.register(Mentor_univ)
admin.site.register(EmailConfirm)


# @admin.register(Univ_category)
# class UnivAdmin(ImportExportModelAdmin):
#     list_display = ('university', 'college', 'department', 'categorized', 'pk')
#     ordering = ['pk']

admin.site.register(Categorized)