# Generated by Django 3.0 on 2019-12-20 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('csharp', '0008_auto_20191220_2129'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingredient',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images', verbose_name='Изображение'),
        ),
    ]
