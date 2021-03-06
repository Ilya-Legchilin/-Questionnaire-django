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
    received_data = request.POST.items()
    data = []
    for i in received_data:
        data.append(i)   
    record = Record()
    
    record.user_id = data[1][1]
    record.questionnaire = data[3][1]
    record.number_of_questions = data[2][1]
    dictionary = {}
    j = 0
    temp_key = 0
    for i in range(4, len(data)):
        temp_tuple = data[i]
        try:
            a = int(temp_tuple[0])
        except ValueError:  
            if temp_tuple[1] == 'on':
                dictionary[temp_key].append(temp_tuple[0])
            else:
                dictionary[temp_key].append(temp_tuple[1])
        else:
            if not dictionary.get(temp_tuple[1]):
                dictionary[temp_tuple[1]] = []
                temp_key = temp_tuple[1]  
    record.dictionary = repr(dictionary)
    record.save()
    return render(request, 'thank.html')
    
    
def show_record(request):
    uid = request.POST.get("special_key")
    record = None
    for temp in Record.objects.all():
        if uid == temp.user_id:
            record = temp
    if record == None:
        return render(request, 'not_found.html')
    else:
        dictionary = eval(record.dictionary)
        return render(request, 'show_record.html', {'record': record, 'dictionary': dictionary})
    
    