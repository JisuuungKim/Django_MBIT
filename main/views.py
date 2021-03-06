from django.shortcuts import render, redirect
from .models import Question, Developer, Choice

def index(request):
    developers = Developer.objects.all()
    #모든 오브젝트를 가져옴

    context = {
        'developers' : developers,
    }

    return render(request, 'main/index.html', context=context)
    #context와 합쳐서 index를 사용자에게 넘겨주겠다

def form(request):
    questions = Question.objects.all()
    #모든 오브젝트를 가져옴

    context = {
        'questions' : questions,
    }

    return render(request, 'main/form.html', context=context)

def submit(request):
    #문항 수
    N = Question.objects.count()
    #개발자 유형 수
    K = Developer.objects.count()

    counter = [0] * (K+1)

    for n in range(1,N+1):
        developer_id = int(request.POST[f'question-{n}'][0])
        counter[developer_id] += 1

    #최고점 개발 유형
    best_developer_id = max(range(1, K+1), key=lambda id: counter[id])
    best_developer = Developer.objects.get(pk=best_developer_id)
    best_developer.count += 1
    best_developer.save()

    context = {
        'developer' : best_developer,
        'counter' : counter
    }
    return redirect('main:result', developer_id = best_developer_id)


def result(request, developer_id):
    developer = Developer.objects.get(pk=developer_id)
    context = {
        'developer' : developer,
    }
    return render(request, 'main/result.html', context = context)

def all_results(request):
    return render(request, 'main/all_results.html')