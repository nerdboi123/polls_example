from django.db import models

# Create your models here.

class Question(models.Model): #추가한 질문들은 question class의 객체가 된다.
    question_text = models.CharField(max_length=200)
    pub_date = models.DateField("date published")

    def __str__(self):
        return self.question_text

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE) #외래키는 다른 키의 기본키에서만 가져올 수 있다.
    choice_text= models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
