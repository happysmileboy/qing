from django.db import models
# Create your models here.


class Notice(models.Model):
    title = models.CharField(max_length=200, verbose_name='제목')
    write_by = models.CharField(max_length=20, verbose_name='글쓴이')
    content = models.TextField(verbose_name='내용')
    created_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title