# Generated by Django 3.2.4 on 2021-06-21 15:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_quiztemp_results'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Results',
            new_name='Result',
        ),
    ]
