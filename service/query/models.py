from django.db import models


class Question(models.Model):
    id = models.IntegerField(primary_key=True)
    question_text = models.CharField(max_length=1000)
    answer_text = models.CharField(max_length=1000)
    created_at = models.DateTimeField()

