from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from datetime import datetime

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
    return render(request, 'index.html', context)


def select(request):
    # message = '수 하나를 입력해주세요.'
    context = {'number': 3}
    # return HttpResponse(message)
    return render(request, 'select.html', context)


def result(request):
    # message = '추첨 결과입니다.'
    context = {'numbers': [1,2,3,4,5,6]}
    # return HttpResponse(message)
    return render(request, 'result.html', context)