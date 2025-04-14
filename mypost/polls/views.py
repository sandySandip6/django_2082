# from django.shortcuts import render

# # Create your views here.

# def index(request):
#     return render(request, 'this is the index page')
from django.http import Http404
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, get_object_or_404
from .models import Question


def polls_index(request):
    latest_question_list = Question.objects.order_by("-post_date")[:5]
    template = loader.get_template("polls/index.html")
    context = {"latest_question_list": latest_question_list}
    return HttpResponse(template.render(context, request))

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/detail.html", {"question": question})

def result(request, qns_id):
    response = "you are looking at the result of question %s."
    return HttpResponse(response%qns_id)

def vote(request, qns_id):
    return HttpResponse("you are voting on %s.", qns_id)


