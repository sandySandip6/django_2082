# from django.shortcuts import render

# # Create your views here.

# def index(request):
#     return render(request, 'this is the index page')
from django.shortcuts import render
from django.http import Http404 
from .models import Question


def polls_index(request):
    latest_question_list = Question.objects.order_by("-post_date")[:5]
    context = {"latest_question_list": latest_question_list}
    return render(request, "polls/index.html",context)

def detail(request, qns_id):
    try:
        question = Question.objects.get(pk = qns_id)
    except Question.DoesNotExist:
        raise Http404("Question Not Found")
    return render(request, "polls/details.html", {"question": question})

def result(request, qns_id):
    response = "you are looking at the result of question %s."
    return render(request, response%qns_id)

def vote(request, qns_id):
    return render(request,"you are voting on %s.", qns_id)