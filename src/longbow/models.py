from django.db import models


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
