from django import forms
from . models import quiz_model,quiz_Question,quiz_answer
from catagories.models import Category_model

class quiz_form(forms.ModelForm):
    class Meta:
        model = quiz_model
        fields = ['title','quiz_description','quiz_category','time_limit','image','quiz_banner']

class quiz_Question_form(forms.ModelForm):
    class Meta:
        model = quiz_Question
        fields = ['quiz','quizQuestion','quizMark','correct_quiz_answer']

class quiz_answer_form(forms.ModelForm):
    class Meta:
        model = quiz_answer
        fields = ['quiz_question','possible_quiz_answer']

class quiz_catagory(forms.ModelForm):
    class Meta:
        model = Category_model
        fields = ['name']