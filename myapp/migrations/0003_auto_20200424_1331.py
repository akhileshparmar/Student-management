# Generated by Django 2.2.6 on 2020-04-24 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_auto_20200421_1347'),
    ]

    operations = [
        migrations.AlterField(
            model_name='students',
            name='Img',
            field=models.ImageField(blank=True, default='IMG', upload_to='media'),
        ),
        migrations.AlterField(
            model_name='students',
            name='Sem1',
            field=models.ImageField(blank=True, default='Not Found', upload_to='media'),
        ),
        migrations.AlterField(
            model_name='students',
            name='Sem2',
            field=models.ImageField(blank=True, default='Not Found', upload_to='media'),
        ),
        migrations.AlterField(
            model_name='students',
            name='Sem3',
            field=models.ImageField(blank=True, default='Not Found', upload_to='media'),
        ),
        migrations.AlterField(
            model_name='students',
            name='Sem4',
            field=models.ImageField(blank=True, default='Not Found', upload_to='media'),
        ),
    ]
