from django.shortcuts import render
from . forms import quiz_form,quiz_Question_form,quiz_answer_form,quiz_catagory

# Create your views here.
def create_quiz(request):
    if request.method== 'POST':
        form = quiz_form(request.POST,request.FILES)
        if form.is_valid():
            form.save()
    else :
        form =  quiz_form()

    return render(request,"create_quiz.html",{'form':form})

def create_question(request):
    if request.method== 'POST':
        form = quiz_Question_form(request.POST)
        if form.is_valid():
            form.save()
    else :
        form =  quiz_Question_form()

    return render(request,"create_question.html",{'form':form})

def create_answer(request):
    if request.method== 'POST':
        form = quiz_answer_form(request.POST)
        if form.is_valid():
            form.save()
    else :
        form =  quiz_answer_form()

    return render(request,"create_answer.html",{'form':form})

def create_category(request):
    if request.method== 'POST':
        form = quiz_catagory(request.POST)
        if form.is_valid():
            form.save()
    else :
        form =  quiz_catagory()

    return render(request,"quiz_catagory.html",{'form':form})



