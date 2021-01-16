from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from datetime import datetime

import random

# Create your views here.
def index(request):
    # HttpResponse: 클래스
    # template = loader.get_template('index.html')
    # 현재 시간
    now = datetime.now()
    context = {
        'current_date': now
    }
    # return HttpResponse(template.render(context, request))
    return render(request, 'first/index.html', context)


def select(request):
    # message = '수 하나를 입력해주세요.'
    # context = {'number': 3}
    context = {}
    # return HttpResponse(message)
    return render(request, 'first/select.html', context)


def result(request):
    # message = '추첨 결과입니다.'
    # context = {'numbers': [1,2,3,4,5,6]}
    # return HttpResponse(message)

    # 사용자가 입력해 넣은 숫자를 가져옴.
    chosen = int(request.GET['number'])

    results = []
    if chosen >= 1 and chosen <= 45:
        results.append(chosen)

    box = []
    for i in range(0, 45):
        if chosen != i+1:
            box.append(i+1)

    random.shuffle(box)

    while len(results) < 6:
        results.append(box.pop())

    # context = {
    #     'numbers': [chosen, 2, 3, 4, 5, 6]
    # }

    context = {
        'numbers': results
    }

    return render(request, 'first/result.html', context)