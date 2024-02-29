from django.shortcuts import render,redirect
from catagories.models import Category_model
from django.http import HttpResponse
from quizes.models import quiz_model,quiz_Question
from catagories.models import Category_model
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import messages
from django.urls import reverse
from django.contrib.sites.shortcuts import get_current_site




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


def catagory_wise_filter(request,category_slug=None):
    quiz_model_details = quiz_model.objects.all()
    if category_slug is not None:
         category_model_slug=Category_model.objects.get(slug = category_slug) #getting the slug field of catagory ? 
         print("printing category slug here :",category_slug)
         quiz_model_details =quiz_model.objects.filter(quiz_category = category_model_slug)
         print("pringitn quiz detils",quiz_model_details)
    quiz_model_all = quiz_model.objects.all()
   

    context = {
        'quiz_model_all':quiz_model_all,
        'filtered_quiz' : quiz_model_details,
        
    }
    return render(request,"home.html",context)

def quiz_view(request,quiz_model_id):
    quiz_questin_filter= get_object_or_404(quiz_model, pk=quiz_model_id)
    questions = quiz_questin_filter.questions_tracker.all()
    PAGINATOR = Paginator( quiz_questin_filter.questions_tracker.all(),1)
    page = request.GET.get('page')
    all_quiz_data_paginator = PAGINATOR.get_page(page)
    context = {
        'filtered_quizes':quiz_questin_filter,
        'questions': questions,
        'all_quiz_data_paginator':all_quiz_data_paginator
    }

    return render(request,"quiz.html",context)

def submit_answer(request,quiz_question_id,page_number=None,quiz_model_id=None):
    # page_number=int(page_number)
    print("quiz question id : ",quiz_question_id)

    # quiz_instance = quiz_Question()
    quiz_answer_model_instance = get_object_or_404(quiz_Question, pk=quiz_question_id)
    correct_answer = quiz_answer_model_instance.correct_quiz_answer


    print("printin correct answer ",correct_answer)
    
    selected_option=[]
    if request.method == 'POST':
        # Assuming your form field name is 'selected_option'
        selected_option = request.POST.get('question1')  #the option or radio button user clcked
        print("user's submission :", selected_option)
        print("printing page number",page_number)
        is_correct =(selected_option == correct_answer) 
        current_site = get_current_site(request)

        if is_correct:
             messages.success(request, 'Correct')
        else:
             messages.error(request, 'incorrect!')
    context = {
        'correct_answer':correct_answer,
        'selected_option':selected_option,
    }   

    # custom_url = f"http://{current_site.domain}/{quiz_model_id}/?page={page_number}"
    # custom_url = f"http://{request.get_host()}/{quiz_model_id}/?page={page_number}"
    # return redirect(custom_url)

    # return redirect(custom_url)
    # return render(request,"quiz.html",context)
    # return redirect("quiz_view", quiz_model_id=quiz_answer_model_instance.quiz.id, page=page_number)
    # return redirect('quiz_view', quiz_model_id=quiz_answer_model_instance.quiz.id)

    try:
        page_number = int(page_number)
    except (TypeError, ValueError):
        page_number = 1  # Set a default value or handle the error as needed

    # Construct the redirect URL dynamically
    current_site = get_current_site(request)
    redirect_url = reverse('quiz_view', kwargs={'quiz_model_id': quiz_model_id})
    redirect_url += f'?page={page_number}'

    return redirect(redirect_url)
    
    


    


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





