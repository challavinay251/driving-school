from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import RealTimeImage
def home(request):
    images = RealTimeImage.objects.all()
    trainers = Trainers.objects.all()
    context = {
        'images': images,
        'trainers': trainers
    }
    return render(request, 'school/home.html', context)

# Driving Lessons page view
def driving_lessons(request):
    return render(request, 'school/driving-lessons.html')

# Lesson and License page view
def lesson_license(request):
    return render(request, 'school/lesson-license.html')


from django.shortcuts import render, redirect
from .forms import InterestForm


# View to handle the interest form submission
def interest_form(request, session_type):
    if request.method == 'POST':
        form = InterestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # Redirect to home or a success page after form submission
    else:
        # Initialize the form with the selected session
        form = InterestForm(initial={'session': session_type})

    return render(request, 'school/interest_form.html', {'form': form, 'session_type': session_type})



from django.shortcuts import render, redirect, get_object_or_404
from .models import Trainers, Review
from .forms import ReviewForm
def add_review(request, trainers_id):
    trainer = get_object_or_404(Trainers, id=trainers_id)
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.trainer = trainer
            review.save()
            return redirect('home')  # Redirect after submitting the review
    else:
        form = ReviewForm()

    return render(request, 'school/add_review.html', {'form': form, 'trainer': trainer})


