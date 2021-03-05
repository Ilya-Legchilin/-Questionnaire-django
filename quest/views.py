from django.shortcuts import render
from .models import Questionnaire, Record
from django.http import HttpResponse


def index(request):
    return render(request, 'main.html')
    
    
def quests(request):
    questionnaires = Questionnaire.objects.all()
    return render(request, 'list.html', {'questionnaires' : questionnaires})
    
    
def storage(request):
    return render(request, 'storage.html')


def quest_pass(request, pk):
    quest = Questionnaire.objects.get(id=pk)
    list_of_questions = []
    for c in quest.question_set.all():
        ans = c.answer_set.all()
        list_of_questions.append((c, ans))
    return render(request, 'pass.html', {'quest': quest, 'list_of_questions': list_of_questions})


def receive_record(request):
    record = Record()
    record.record_user_id = request.POST.get("user_id")
    return HttpResponse("something happend")