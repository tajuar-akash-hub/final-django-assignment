from django.shortcuts import render
from catagories.models import Category_model
from django.http import HttpResponse
from quizes.models import quiz_model,quiz_Question
from catagories.models import Category_model
from django.shortcuts import render, get_object_or_404


# Create your views here.
def home(request):
    quiz =quiz_model.objects.all()
    quiz_question = quiz_Question.objects.all()
    catagory_all_for_browse= Category_model.objects.all()
    context={
        'quizes':quiz,
        'question':quiz_question,
        'category':catagory_all_for_browse,

    }
    
    return render(request,"home.html",context)




def quiz_view(request,id):
    # quiz_questin_filter= quiz_Question.objects.filter(id=id)

    quiz_questin_filter= get_object_or_404(quiz_model, pk=id)
    questions = quiz_questin_filter.questions_tracker.all()
    # correct_answer =questions.questions_tracker.correct_quiz_answer

    # bringing data frontend to backend
    # if request.method == 'POST':
    #     print("printing post",request.POST)
    context = {
        'filtered_quizes':quiz_questin_filter,
        'questions': questions,
       
    }

    return render(request,"quiz.html",context)


def catagory_wise_filter(request,category_slug=None):
    
    quiz_model_details = quiz_model.objects.all()
    if category_slug is not None:
         category_model_slug=Category_model.objects.get(slug = category_slug) #getting the slug field of catagory ? 
         print("printing category slug here :",category_slug)
         quiz_model_details =quiz_model.objects.get(quiz_category = category_model_slug)
         print(quiz_model_details)

        
    quiz_model_all = quiz_model.objects.all()

    context = {
        'filtered_quiz' : quiz_model_details,
        

    }

    return render(request,"home.html",context)
        
         
    

def submit_answer(request):
    print(request.POST.cleaned_data[''])
    return render(request,"quiz_response.html")


# def quiz_view(request, category_slug):
#     # Assuming you have a Category model with a 'slug' field
#     category = get_object_or_404(Category_model, slug=category_slug)

#     # Assuming you have a Quiz model with a 'category' field
#     quiz = get_object_or_404(quiz_model, category=category)
#     questions = quiz_Question.objects.filter(quiz=quiz)
#     totalMarksOfAllQuestions = sum(question.quizMark for question in questions)

#     if request.method == 'POST':
#         # Handle form submission for each question
#         score = 0
#         totalMarks = 0
#         selected_choices = []
#         for question in questions:
#             totalMarks += question.quizMark
#             selected_choice_id = request.POST.get(
#                 f'question_{question.id}_choice')

#             selected_choice = get_object_or_404(Choice, id=selected_choice_id)
#             selected_choices.append(selected_choice)

#             # Check if the selected choice is correct
#             if selected_choice.is_correct:
#                 # score += 1
#                 score += question.quizMark

#         # Save user quiz history
#         user_quiz_history = UserQuizHistory(
#             user=request.user, quiz=quiz, score=score, totalMarks=totalMarks)
#         user_quiz_history.save()
#         user_quiz_history.selected_choices.set(selected_choices)

#         # Send email to the user
#         subject = 'Quiz Completion'
#         # message = f'Thank you for completing the quiz "{quiz.title}". Your score is {score}/{len(questions)}.'
#         message = f'Thank you for completing the quiz "{quiz.title}". Your score is {score}/{totalMarks}.'
#         from_email = EMAIL_HOST_USER
#         recipient_list = [request.user.email]

#         send_mail(subject, message, from_email,
#                   recipient_list, fail_silently=False)

#         return redirect('quiz_result', quiz_id=quiz.id)

#     context = {
#         'quiz': quiz,
#         'questions': questions,
#         'totalMarksOfAllQuestions': totalMarksOfAllQuestions
#     }
#     return render(request, 'quiz.html', context)













# def home(request,book_model_slug=None):

#     book_model_detials = Book_model.objects.all()
#     if book_model_slug is not None:
#         book_mode_slug_field= Category_model.objects.get(slug=book_model_slug)
#         book_model_detials= Book_model.objects.filter(categories=book_mode_slug_field)

#     catagory_details = Category_model.objects.all()
#     return render(request,"./home.html",{'catagory_details':catagory_details,'book_model_detials':book_model_detials})





