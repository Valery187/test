from django.urls import path

from .views import index, lessonFour

urlpatterns = [
    path('', index),
    path('lesson_4/', lessonFour)
]
