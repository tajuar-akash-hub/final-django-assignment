from django import forms
from . models import quiz_model,quiz_Question,quiz_answer,Quiz_rating_model
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




RATING_CHOICES = [
    (1, '1'),
    (2, '2'),
    (3, '3'),
    (4, '4'),
    (5, '5'),
    (6, '6'),
    (7, '7'),
]
class Quiz_Rating_Form(forms.ModelForm):
    rating = forms.ChoiceField(
        choices=RATING_CHOICES,
        widget=forms.RadioSelect(attrs={'class': 'form-check-input'}),
        required=True,
    )
    class Meta:
        model = Quiz_rating_model
        fields = ['quiz_rating']