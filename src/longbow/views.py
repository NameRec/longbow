from django import forms
from django.http import HttpResponseForbidden
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User

from longbow.models import Test, TestPassing
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

    def get_answers_input_type(answers):
        correct_answers = 0
        for answer in answers:
            if answer.is_answer_correct:
                correct_answers += 1
            if correct_answers > 1:
                break
        return 'radio' if correct_answers < 2 else 'checkbox'

    # At first, check for TestPassing exists, and linked to current user.
    passing: TestPassing = get_object_or_404(TestPassing, pk=passing_id)
    if passing.user.id != request.user.id:
        raise HttpResponseForbidden()

    # Next, if test completed - redirect to statistics page
    if passing.completion_time is not None:
        return redirect('test-details', test_id=passing.test.id)

    # Ok, working...
    current_question = passing.get_questions_to_pass().order_by('order').first()
    answers = [answer for answer in current_question.answer_set.all()]
    input_type = get_answers_input_type(answers)
    errors = None
    if request.method == 'POST':
        user_choice = request.POST.getlist('answer')
        if len(user_choice) == 0:
            errors = 'You should make answer. Select one{} from offered variants.'.format(
                '' if input_type == 'radio' else ' or more'
            )

        if errors is None:
            # success: save user answer(s)
            passing.save_user_choice(
                current_question,
                list(filter(lambda answer: str(answer.id) in user_choice, answers))
            )
            if passing.completion_time is not None:
                # test is complete - redirect to statistics
                return redirect('test-details', test_id=passing.test.id)
            else:
                # go to next question
                return redirect('test-passing', passing_id=passing.id)

        # there we have errors: show input form with errors
        def restore_answers_order(answers: list, order: str):
            # on GET request, list offered answers are shuffled (see below) - if we return form to user, we need
            # provide answers order same as before
            result = [None] * len(answers)
            order_list = list(map(lambda x: int(x), order.split(',')))
            for answer in answers:
                result[order_list.index(answer.id)] = answer
            return result

        order = request.POST['order']
        answers = restore_answers_order(answers, order)
    else:
        shuffle(answers)
        order = ','.join([str(answer.id) for answer in answers])

    return render(request, 'longbow/test_passing.html', {
        'question_no': passing.get_passed_questions().count() + 1,
        'questions_count': passing.get_all_test_questions().count(),
        'question': current_question.question_text,
        'input_type': input_type,
        'order': order,
        'answers': answers,
        'errors': errors,
    })


@login_required
def test_start(request, test_id: int):
    if request.method == 'POST':
        form = forms.Form(request.POST)
        if form.is_valid():
            passing = TestPassing(
                user=User.objects.get(pk=request.user.id),
                test=Test.objects.get(pk=test_id),
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
