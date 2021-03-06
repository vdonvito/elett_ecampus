# Generated by Django 3.2.4 on 2021-06-16 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='QuizTemp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('domanda', models.CharField(max_length=1000)),
                ('r1', models.CharField(max_length=1000)),
                ('r2', models.CharField(max_length=1000)),
                ('r3', models.CharField(max_length=1000)),
                ('r4', models.CharField(max_length=1000)),
                ('rc', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Results',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('domanda', models.CharField(max_length=1000)),
                ('r1', models.CharField(max_length=1000)),
                ('r2', models.CharField(max_length=1000)),
                ('r3', models.CharField(max_length=1000)),
                ('r4', models.CharField(max_length=1000)),
                ('rispostaData', models.CharField(max_length=1000)),
                ('rc', models.CharField(max_length=1000)),
            ],
        ),
    ]
