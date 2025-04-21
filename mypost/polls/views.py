
from django.shortcuts import render , get_object_or_404
from django.http import Http404
from .models import Question, Choice
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.db.models import F


def polls_index(request):
    latest_question_list = Question.objects.order_by("-post_date")[:5]
    context = {"latest_question_list": latest_question_list}
    return render(request, "polls/index.html",context)

def details(request, qns_id):
    try:
        question = Question.objects.get(pk = qns_id)
    except Question.DoesNotExist:
        raise Http404("Question Not Found")
    return render(request, "polls/details.html", {"question": question})

def results(request, qns_id):
    question = get_object_or_404(Question, pk=qns_id)
    return render(request, "polls/results.html", {"question": question})

def vote(request, qns_id):
    question = get_object_or_404(Question, pk=qns_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(
            request,
            "polls/details.html",
            {
                "question": question,
                "error_message": "You didn't select a choice.",
            },
        )
    else:
        selected_choice.votes = F("votes") + 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))


