from django.shortcuts import render
from OnlineQuiz.models import Quiz

def quizonline(request):
    results=Quiz.objects.all()
    return render(request,'index.html',{"Quiz":results})
    