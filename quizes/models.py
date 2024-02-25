from django.db import models
from catagories.models import Category_model
from django.contrib.auth.models import User
from . constant import rating_list

# Create your models here.
class quiz_model(models.Model):
    title = models.CharField(max_length=50)
    quiz_description = models.CharField( max_length=50)
    quiz_category = models.ForeignKey(Category_model , on_delete=models.CASCADE)
    time_limit = models.BooleanField(default=False)
    creation_time = models.DateField( auto_now_add=True)
    update_time = models.DateField(auto_now=True)
    image = models.ImageField( upload_to=None, height_field=None, null=True,blank=True)
    quiz_banner = models.ImageField(upload_to=None, blank=True,null=True)
    def __str__(self) -> str:
        return f'{self.title}'
    
class quiz_Question(models.Model):
    quiz = models.ForeignKey(quiz_model, on_delete=models.CASCADE, related_name='questions_tracker', default=1)
    quizQuestion = models.CharField(max_length=255)
    quizMark = models.IntegerField(default=1)
    correct_quiz_answer = models.CharField(blank=True,null=True,max_length=50)
    def __str__(self):
        return f'{self.quizQuestion} and {self.correct_quiz_answer}'
    
class quiz_answer(models.Model):
    quiz_question = models.ForeignKey(quiz_Question,related_name="answer_tracker" , on_delete=models.CASCADE)
    possible_quiz_answer = models.CharField(blank=True,null=True,max_length=50)
   
    def __str__(self) -> str:
        return f'{self.quiz_question} possible answer : {self.possible_quiz_answer}'



class Quiz_rating_model(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quiz = models.ForeignKey(quiz_model, on_delete=models.CASCADE)
    quiz_rating = models.PositiveIntegerField(choices=rating_list)

    def __str__(self):
        return f'{self.user.username} - {self.quiz.title} - {self.rating}'





class Choice(models.Model):
    quiz_question = models.ForeignKey(quiz_Question, on_delete=models.CASCADE)
    quiz_Answer = models.CharField(max_length=255)
    is_correct = models.BooleanField(default=False)
    def __str__(self):
        return f'{self.quiz_question.quizQuestion} ----- {self.quiz_Answer}'
    
class quiz_history_of_user(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quiz = models.ForeignKey(quiz_model, on_delete=models.CASCADE)
    score = models.IntegerField()
    totalMarks = models.IntegerField(default=0)
    completed_time = models.DateTimeField(auto_now_add=True)
    selected_choices = models.ManyToManyField(Choice, related_name='selected_choices', blank=True)
    certificate = models.FileField(upload_to='certificates/', blank=True, null=True)
    def __str__(self):
        return self.user.username

