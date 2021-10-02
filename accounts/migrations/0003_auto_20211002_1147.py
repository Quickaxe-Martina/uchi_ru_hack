# Generated by Django 3.2.7 on 2021-10-02 08:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='birthday',
            field=models.DateField(blank=True, null=True, verbose_name='День рождения'),
        ),
        migrations.AddField(
            model_name='customuser',
            name='instagram',
            field=models.URLField(blank=True, null=True, verbose_name='Инстаграм'),
        ),
        migrations.AddField(
            model_name='customuser',
            name='referral',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='customuser',
            name='role',
            field=models.CharField(blank=True, choices=[('teacher', 'Учитель'), ('student', 'Ученик')], default='student', max_length=50, verbose_name='Роль'),
        ),
    ]