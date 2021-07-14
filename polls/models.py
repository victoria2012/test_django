from django.db import models

# Create your models here.

class Question(models.Model):  # 각 컬럼의 타입을
    question_text = models.CharField(max_length=100)
    public_date = models.DateTimeField()
    votes = models.BigIntegerField()
