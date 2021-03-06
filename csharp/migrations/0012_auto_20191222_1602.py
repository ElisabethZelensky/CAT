# Generated by Django 2.2.8 on 2019-12-22 13:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('csharp', '0011_auto_20191220_2223'),
    ]

    operations = [
        migrations.AddField(
            model_name='operationspecification',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='Описание'),
        ),
        migrations.CreateModel(
            name='EquipmentFailures',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('failure_date', models.DateTimeField(auto_now_add=True, verbose_name='Время начала сбоя')),
                ('causes', models.CharField(choices=[('Причина 1', 'Причина 1'), ('Причина 2', 'Причина 2'), ('Причина 3', 'Причина 3')], default='Причина 1', max_length=200, verbose_name='Причина сбоя')),
                ('failure_date_over', models.DateTimeField(blank=True, null=True, verbose_name='Время продолжения работы')),
                ('equipment', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='csharp.Equipment', verbose_name='Оборудование')),
            ],
        ),
    ]
