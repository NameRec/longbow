from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from typing import List


class Test(models.Model):
    description = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        repr_ = self.description
        if self.pub_date:
            repr_ += f' @{self.pub_date}'
        return repr_


class Question(models.Model):
    test = models.ForeignKey(Test, on_delete=models.CASCADE)
    question_text = models.CharField(max_length=255)
    order = models.PositiveIntegerField(default=0, blank=False, null=False)

    def __str__(self):
        return self.question_text


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer_text = models.CharField(max_length=255)
    is_answer_correct = models.BooleanField(default=False)
    order = models.PositiveIntegerField(default=0, blank=False, null=False)

    class Meta:
        ordering = ('order',)

    def __str__(self):
        return '"{}" - {}'.format(self.answer_text, 'correct' if self.is_answer_correct else 'incorrect')


class TestPassing(models.Model):
    test = models.ForeignKey(Test, related_name='+', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='+', on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    completion_time = models.DateTimeField(null=True)
    stat_count_questions = models.PositiveIntegerField(default=0, blank=False, null=True)
    stat_correct_answers = models.PositiveIntegerField(default=0, blank=False, null=True)

    class Meta:
        unique_together = ('test', 'user')

    def get_all_test_questions(self):
        return self.test.question_set.all()

    def get_passed_questions(self):
        return TestPassingQuestion.objects.filter(test_passing__exact=self.id).values('question')

    def get_questions_to_pass(self):
        return self.get_all_test_questions().exclude(pk__in=self.get_passed_questions())

    def save_user_choice(self, question: Question, answers: List[Answer]):
        passing_question = self.testpassingquestion_set.create(question=question, answer_time=timezone.now())
        passing_question.save()
        for answer in answers:
            passing_question.testpassinganswer_set.create(answer=answer).save()

        # check: is the test completed? If yes, collect statistics, and update TestPassing record
        if self.get_questions_to_pass().count() == 0:
            self.completion_time = timezone.now()

            # <FIXME> It's wild... For this you need SQL...
            correct_answers: int = 0
            for question in self.testpassingquestion_set.all():
                if question.is_answer_correct():
                    correct_answers += 1
            self.stat_correct_answers = correct_answers
            self.stat_count_questions = self.get_all_test_questions().count()
            self.save()


class TestPassingQuestion(models.Model):
    test_passing = models.ForeignKey(TestPassing, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, related_name='+', on_delete=models.CASCADE)
    answer_time = models.DateTimeField()

    def is_answer_correct(self):
        # <FIXME> It's wild... For this you need SQL...
        user_answers = set(map(lambda user_answer: user_answer.answer.id, self.testpassinganswer_set.all()))
        correct_answers = set(map(lambda answer: answer.id, self.question.answer_set.filter(is_answer_correct__exact=True)))
        return user_answers == correct_answers


class TestPassingAnswer(models.Model):
    test_passing_question = models.ForeignKey(TestPassingQuestion, on_delete=models.CASCADE)
    answer = models.ForeignKey(Answer, related_name='+', on_delete=models.CASCADE)

    class Meta:
        unique_together = ('test_passing_question', 'answer')
