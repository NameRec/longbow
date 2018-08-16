from django import forms
from django.http import Http404
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.utils import timezone

from longbow.models import Test, Question, TestPassing, TestPassingQuestion
from random import shuffle


class IndexView(LoginRequiredMixin, ListView):
    template_name = 'longbow/index.html'

    def get_queryset(self):
        return Test.objects.all().order_by('-pub_date')


def get_test_passing(request, test_id: int) -> object:
    try:
        return TestPassing.objects.get(test=test_id, user=request.user.id)
    except TestPassing.DoesNotExist:
        return None


@login_required
def test_details(request, test_id: int):
    passing = get_test_passing(request, test_id)
    if passing is None:
        return redirect('test-start', test_id=test_id)
    elif passing.completion_time is None:
        return redirect('test-passing', passing_id=passing.id)
    else:
        return render(request, 'longbow/test_details.html', context={'passing': passing})


@login_required
def test_passing(request, passing_id: int):

    def get_passing_state():
        # At first check for TestPassing exists, and linked to current user.
        try:
            passing = TestPassing.objects.get(pk=passing_id)
        except TestPassing.DoesNotExist:
            raise Http404()
        if passing.user.id != request.user.id:
            raise Http404()

        # Next, if test completed - redirect to statistics page
        if passing.completion_time is not None:
            return redirect('test-details', test_id=passing.test.id)

        # Ok, now determine the question to be answered
        passed_questions_qs = TestPassingQuestion.objects.filter(test_passing__exact=passing.test.id).values('question')
        all_test_questions_qs = Question.objects.filter(test__exact=passing.test.id)
        questions_qs = all_test_questions_qs\
            .filter(test__exact=passing.test.id)\
            .exclude(pk__in=passed_questions_qs)\
            .order_by('order')
        return all_test_questions_qs.count(), passed_questions_qs.count() + 1, questions_qs.first()

    def get_answers_input_type(answers):
        correct_answers = 0
        for answer in answers:
            if answer.is_answer_correct:
                correct_answers += 1
            if correct_answers > 1:
                break
        return 'radio' if correct_answers == 1 else 'checkbox'

    count_questions, current_question_number, current_question = get_passing_state()
    answers = [answer for answer in current_question.answer_set.all()]
    shuffle(answers)

    if request.method == 'POST':
        answers = request.POST.getlist('answer')
        return render(request, 'print.html', {'message': f'answer: {request.POST["answer"]}'})
    else:
        return render(request, 'longbow/test_passing.html', {
            'question_no': current_question_number,
            'questions_count': count_questions,
            'question': current_question.question_text,
            'input_type': input_type,
            'answers': answers,
        })


@login_required
def test_start(request, test_id: int):
    if request.method == 'POST':
        form = forms.Form(request.POST)
        if form.is_valid():
            passing = TestPassing(
                user=User.objects.get(pk=request.user.id),
                test=Test.objects.get(pk=test_id),
                start_time=timezone.now()
            )
            passing.save()
            return redirect('test-details', test_id=test_id)
    else:
        # handle scenario, when user explicitly specified url in browser address line
        if get_test_passing(request, test_id) is not None:
            return redirect('test-details', test_id=test_id)
        form = forms.Form()
        form.test_description = Test.objects.get(pk=test_id).description
    return render(request, 'longbow/test_new_passing.html', {'form': form})
