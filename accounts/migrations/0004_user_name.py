# Generated by Django 2.0.2 on 2018-03-13 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20180311_1433'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='name',
            field=models.CharField(default=None, max_length=10, verbose_name='이름'),
            preserve_default=False,
        ),
    ]
