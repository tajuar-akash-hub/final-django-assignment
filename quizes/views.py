from django.shortcuts import render
from . forms import quiz_form

# Create your views here.
def create_quiz(request):
    if request.method== 'POST':
        form = quiz_form(request.POST,request.FILES)
        if form.is_valid():
            form.save()
    else :
        form =  quiz_form()

    return render(request,"create_quiz.html",{'form':form})



