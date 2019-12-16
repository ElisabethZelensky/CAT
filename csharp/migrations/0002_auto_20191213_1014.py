# Generated by Django 3.0 on 2019-12-13 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('csharp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ingredient',
            name='articul',
            field=models.CharField(default=0, max_length=20, unique=True),
        ),
        migrations.AddField(
            model_name='ingredient',
            name='name',
            field=models.CharField(default='Введите наименование ингредиента', max_length=20),
        ),
        migrations.AddField(
            model_name='provider',
            name='name',
            field=models.CharField(default='Поставщик', max_length=1024),
        ),
    ]
