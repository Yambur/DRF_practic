from django.urls import path
from rest_framework import routers

from classes.views.course import CourseViewSet
from classes.views.lesson import LessonListView, LessonDetailView, LessonUpdateView, LessonCreateView, LessonDeleteView

urlpatterns = [
    path('lesson/', LessonListView.as_view()),
    path('lesson/<int:pk>/', LessonDetailView.as_view()),
    path('lesson/<int:pk>/update/', LessonUpdateView.as_view()),
    path('lesson/create/', LessonCreateView.as_view()),
    path('lesson/<int:pk>/delete/', LessonDeleteView.as_view()),
]

router = routers.SimpleRouter()
router.register('course', CourseViewSet)

urlpatterns += router.urls