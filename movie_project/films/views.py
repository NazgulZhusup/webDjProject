from django.shortcuts import render, redirect
from .models import New_review
from .forms import Review_Form

def home(request):
    reviews = New_review.objects.all()
    return render(request, 'films/movie_review.html', {'reviews': reviews})

def create_review(request):
    error = ""
    if request.method == 'POST':
        form = Review_Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('reviews_home')
        else:
            error = "Данные заполнены некорректно"
    else:
        form = Review_Form()
    return render(request, 'films/add_review.html', {'form': form, 'error': error})
