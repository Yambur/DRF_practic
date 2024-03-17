from rest_framework import viewsets
from rest_framework.viewsets import ModelViewSet

from classes.models import Course
from classes.serializers.course import CourseSerializers


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializers
