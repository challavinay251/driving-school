from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('driving-lessons/', views.driving_lessons, name='driving_lessons'),  # Driving Lessons page
    path('lesson-license/', views.lesson_license, name='lesson_license'),  # Lesson and License page
    path('interest/<str:session_type>/', views.interest_form, name='interest_form'),
    path('add-review/<int:trainers_id>/', views.add_review, name='add_review'),
]
