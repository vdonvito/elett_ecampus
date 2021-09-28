from django.db import models
from datetime import date

# Create your models here.
class DC(models.Model):
    domanda = models.CharField(max_length=1000)
    image = models.ImageField(upload_to="static/images/", default='default.jpg')
    r1 = models.CharField(max_length=1000)
    r2 = models.CharField(max_length=1000)
    r3 = models.CharField(max_length=1000)
    r4 = models.CharField(max_length=1000)
    rc = models.CharField(max_length=1000)

    def __str__(self):
        return self.domanda

class QuizTemp(models.Model):
    domanda = models.CharField(max_length=1000)
    r1 = models.CharField(max_length=1000)
    r2 = models.CharField(max_length=1000)
    r3 = models.CharField(max_length=1000)
    r4 = models.CharField(max_length=1000)
    rc = models.CharField(max_length=1000)

    def __str__(self):
        return self.domanda

class Result(models.Model):
    domanda = models.CharField(max_length=1000)
    r1 = models.CharField(max_length=1000)
    r2 = models.CharField(max_length=1000)
    r3 = models.CharField(max_length=1000)
    r4 = models.CharField(max_length=1000)
    rc = models.CharField(max_length=1000)

    rispostaData = models.CharField(max_length=1000)
    correct = models.BooleanField(default=False)

    def __str__(self):
        return self.domanda

class Storico(models.Model):
    score = models.IntegerField()
    passed = models.BooleanField(default=False)
    date = models.DateField(default=date.today)

    def __str__(self):
        return "{} Score: {}".format(self.date, self.score)

class DA(models.Model):
    domanda = models.CharField(max_length=1000)
    risposta = models.CharField(max_length=3000)
    image = models.ImageField(upload_to="static/images/", default='default.jpg')
    
    def __str__(self):
        return self.domanda
