
from django.urls import path
from . import views

urlpatterns = [
    
    path('create/quiz', views.create_quiz,name='create_quiz'),
    path('create/question', views.create_question,name='create_question'),
    path('create/answer', views.create_answer,name='create_answer'),
    path('create/category', views.create_category,name='create_category'),

    

]
