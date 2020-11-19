from django.db import models

class Quiz(models.Model):
    Question=models.CharField(max_length=1000)
    Option1=models.CharField(max_length=100)
    Option2=models.CharField(max_length=100)
    Option3=models.CharField(max_length=100)
    Option4=models.CharField(max_length=100)
    CorrectAns=models.CharField(max_length=100)
    class Meta:
        db_table="onlinequiz"
