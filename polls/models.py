from django.db import models

# Create your models here.
# 모델을 생성할 떄는 model.py와 admin.py를 모두 수정해줘야 한다.
# 두 파일 모두 수정했다면 cmd에서 migrate 하여 DB에 반영해야함

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text