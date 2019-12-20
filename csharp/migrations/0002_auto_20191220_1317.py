# Generated by Django 3.0 on 2019-12-20 10:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('csharp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='completion_date',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Плановая дата завершения'),
        ),
        migrations.AlterField(
            model_name='order',
            name='cost',
            field=models.FloatField(verbose_name='Стоимость'),
        ),
        migrations.AlterField(
            model_name='order',
            name='manager',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='manager', to=settings.AUTH_USER_MODEL, verbose_name='Ответственный менеджер'),
        ),
        migrations.AlterField(
            model_name='order',
            name='work_examples',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Примеры работ'),
        ),
    ]
