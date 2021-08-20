from django.shortcuts import render
from django.http import HttpResponse
from .models import Question
from django.template import loader
# Create your views here.
from django.http import HttpResponse
from django.template import loader
import requests
from bs4 import BeautifulSoup
from .models import Question


# def index(request):
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     context = {'latest_question_list': latest_question_list}
#     return render(request, 'polls/base.html', context)
def index(request):


    req = requests.get('https://ncov.moh.gov.vn/', verify=False)
    soup = BeautifulSoup(req.text, "lxml")

    # print(soup.find("div", {"id":"sailorTableArea"}))
    arr = []
    for i in soup.findAll("td", {"class": "text-danger-new"}):
        num = i.text
        if num == 0:
            num = 0
        else:
            if "." in num:
                num = num.replace(".", "")
            if '+' in num:
                num = num[1:]
        arr.append(int(num))
    return HttpResponse("số ca nhiễm trong ngày: " + str(sum(arr)))

def detail(request, question_id):
    return HttpResponse("you are looking at the question: %s" % question_id)

def results(request, question_id):
    response = "you are looking at the question: %s"
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)

