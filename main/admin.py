from django.contrib import admin

# Register your models here.
from main.models import DA, DC, QuizTemp, Result, Storico

admin.site.register(DA)
admin.site.register(DC)
admin.site.register(QuizTemp)
admin.site.register(Result)
admin.site.register(Storico)
