# Generated by Django 2.2.8 on 2020-01-25 09:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('csharp', '0015_auto_20200125_1243'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equipmentfailures',
            name='equipment',
            field=models.ForeignKey(default=5, on_delete=django.db.models.deletion.CASCADE, to='csharp.Tool', verbose_name='Оборудование'),
        ),
    ]