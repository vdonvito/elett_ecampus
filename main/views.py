from django import template
from django.shortcuts import render, redirect, get_object_or_404
from urllib import request
from .models import DC, DA, QuizTemp, Result, Storico
from .forms import QuestionForm

# Create your views here.
def index(request):
    return render (request, "main/index.html")

def delete_all(request):
    entries = DC.objects.all()
    entries.delete()
    entries = DA.objects.all()
    entries.delete()
    entries = QuizTemp.objects.all()
    entries.delete()
    entries = Result.objects.all()
    entries.delete()
    entries = Storico.objects.all()
    entries.delete()

def add(request):
    inp = None
    index = 0
    file_location = "/home/v/Scrivania/SD_INIA10_0128a_02_p2.txt"
    with open(file_location, "r") as f:
        lines = f.readlines()
        while inp != "e":
            print(lines[index])
            print(lines[index+1])
            print(lines[index+2])
            print(lines[index+3])
            print(lines[index+4])

            inp = input("DOMANDA APERTA? Y or N: ").lower()
            if inp=="n":
                print("SCEGLIERE RISPOSTA CORRETTA. 1,2,3,4: ")
                inp = input()
                inp_ris = int(inp)
                d = DC()
                d.domanda = lines[index]
                d.r1 = lines[index+1]
                d.r2 = lines[index+2]
                d.r3 = lines[index+3]
                d.r4 = lines[index+4]
                d.rc = lines[index+inp_ris]
                if 'figura' in d.domanda:
                    n_figura = input('Inserire numero immagine: ')
                    d.image = 'static/images/image-' + n_figura + '.png'
                d.save()

                index+=5

                print("#"*20)
                print("#"*20)
            elif inp=="y" or inp=="s":
                d = DA()
                d.domanda = lines[index]
                d.risposta = "DA INSERIRE"
                if 'figura' in d.domanda:
                    n_figura = input('Inserire numero immagine: ')
                    d.image = 'static/images/image-' + n_figura + '.png'
                d.save()

                index+=1

                print("#"*20)
                print("#"*20)
            else:
                print("SCEGLIERE Y or N. RIPETO ULTIMA DOMANDA.")
    #return redirect('index')

def start(request):
    if request.method=="GET":
        if len(QuizTemp.objects.all()) > 0:
            questions = QuizTemp.objects.all()
        else:
            questions = DC.objects.order_by("?")[:30]
            for q in questions:
                qt = QuizTemp()
                qt.domanda = q.domanda
                qt.r1 = q.r1
                qt.r2 = q.r2
                qt.r3 = q.r3
                qt.r4 = q.r4
                qt.rc = q.rc
                qt.save()
        return render(request, "main/start.html", {"questions":questions})
    else:
        return redirect('quiz')

def quiz(request):
    if request.method=="GET":
        q = QuizTemp.objects.all()[0]
        num = 31 - len(QuizTemp.objects.all())
        return render(request, "main/quiz.html", {"q":q, "num":num})
    else:
        q = QuizTemp.objects.all()[0]
        r = Result()
        r.domanda = q.domanda
        r.r1 = q.r1
        r.r2 = q.r2
        r.r3 = q.r3
        r.r4 = q.r4
        r.rc = q.rc
        r.rispostaData = request.POST.get('answer').strip()
        r.save()

        QuizTemp.objects.filter(id=q.pk).delete()

        if len(QuizTemp.objects.all()) > 0:
            return redirect('quiz')
        else:
            return redirect('result')

def result(request):
    if request.method == "GET":
        if len(QuizTemp.objects.all()) > 0:
            return redirect(result_error)
        else:
            results = Result.objects.all()
            score = 0

            for r in results:
                r.r1 = r.r1.strip()
                r.r2 = r.r2.strip()
                r.r3 = r.r3.strip()
                r.r4 = r.r4.strip()
                r.rc = r.rc.strip()
                r.rispostaData = r.rispostaData.strip()
                if r.rc == r.rispostaData:
                    print("corretto")
                    r.correct = True
                    r.save()
                    score+=1
            if score >= 18:
                message = "PROMOSSO"
            else:
                message = "NON PASSATO"
            return render(request, "main/result.html",{"results":results, "score":score, "message":message})
    else:
        s = Storico()
        results = Result.objects.all()
        score = 0
        for r in results:
            if r.correct == True:
                score+=1
        s.score = score
        if score >= 18:
            s.passed = True
        s.save()
        entries = Result.objects.all()
        entries.delete()
        return redirect('storico')
def storico(request):
    return render(request, "main/storico.html")

def result_error(request):
    if request.method=="GET":
        message = "HAI ANCORA {} DOMANDE A CUI RISPONDERE.".format(len(QuizTemp.objects.all()))
        return render(request, "main/result_error.html",{"message":message})
    else:
        return redirect('quiz')

def prnt(request):
    dom = DA.objects.all()
    for d in dom:
        print(d.domanda)
        print(d.risposta)
        print("#################")

def view_all(request):
    d_ap = DA.objects.all()
    d_ch = DC.objects.all()
    return render(request, "main/view_all.html", {"d_ap":d_ap, "d_ch":d_ch})
