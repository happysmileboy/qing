# Generated by Django 2.0.2 on 2018-03-11 05:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20180310_2030'),
    ]

    operations = [
        migrations.CreateModel(
            name='Univ_category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('university', models.CharField(max_length=20, verbose_name='대학교')),
                ('college', models.CharField(max_length=20, verbose_name='단과대학')),
                ('department', models.CharField(max_length=20, verbose_name='학부, 학과')),
                ('categorized', models.CharField(max_length=20, verbose_name='분류')),
            ],
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(blank=True, max_length=254, verbose_name='이메일'),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=20, unique=True, verbose_name='아이디'),
        ),
        migrations.AddField(
            model_name='mentor_univ',
            name='univ_category',
            field=models.ManyToManyField(to='accounts.Univ_category'),
        ),
    ]
