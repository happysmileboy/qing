from django.contrib import admin
from .models import User, Mentor_univ, EmailConfirm, Univ_category
# Register your models here.

admin.site.register(User)
admin.site.register(Mentor_univ)
admin.site.register(EmailConfirm)


@admin.register(Univ_category)
class Drama2Admin(admin.ModelAdmin):
    list_display = ('university', 'college', 'department', 'categorized', 'pk')
    ordering = ['pk']