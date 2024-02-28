

from django.urls import path,include
from . import views


urlpatterns = [
    path('', views.home,name="home" ),
    path('quiz/<int:quiz_model_id>/', views.quiz_view,name="quiz_view" ),
    path('quiz/submit/<int:quiz_question_id>', views.submit_answer,name="submit_answer" ),
    path('quiz/filter/<slug:category_slug>', views.catagory_wise_filter,name="catagory_wise_filter" ),

    # path('quiz/<int:quiz_model_id>/<int:question_id>/', views.quiz_view,name="quiz_view" ),
    
]
