from django.db import models
from django.contrib.auth.models import User


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

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.question_text


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer_text = models.CharField(max_length=255)
    is_answer_correct = models.BooleanField(default=False)
    order = models.PositiveIntegerField(default=0, blank=False, null=False)

    class Meta:
        ordering = ['order']

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


class TestPassingQuestion(models.Model):
    test_passing = models.ForeignKey(TestPassing, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, related_name='+', on_delete=models.CASCADE)
    answer_time = models.DateTimeField()


class TestingPassingAnswer(models.Model):
    test_passing_question = models.ForeignKey(TestPassingQuestion, on_delete=models.CASCADE)
    answer = models.ForeignKey(Answer, related_name='+', on_delete=models.CASCADE)

    class Meta:
        unique_together = ('test_passing_question', 'answer')
