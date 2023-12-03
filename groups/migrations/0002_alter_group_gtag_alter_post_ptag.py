# Generated by Django 4.2.7 on 2023-12-01 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='gtag',
            field=models.CharField(choices=[('Untitled', 'Untitled'), ('Education', 'Education'), ('Travel', 'Travel'), ('Work', 'Work'), ('Sports', 'Sports'), ('Food', 'Food'), ('Reading', 'Reading'), ('Art', 'Art'), ('Pets', 'Pets'), ('Movies', 'Movies'), ('Music', 'Music'), ('Health', 'Health'), ('Technology', 'Technology')], default='Untitled', max_length=20),
        ),
        migrations.AlterField(
            model_name='post',
            name='ptag',
            field=models.CharField(choices=[('Untitled', 'Untitled'), ('Education', 'Education'), ('Travel', 'Travel'), ('Work', 'Work'), ('Sports', 'Sports'), ('Food', 'Food'), ('Reading', 'Reading'), ('Art', 'Art'), ('Pets', 'Pets'), ('Movies', 'Movies'), ('Music', 'Music'), ('Health', 'Health'), ('Technology', 'Technology')], default='Untitled', max_length=20),
        ),
    ]