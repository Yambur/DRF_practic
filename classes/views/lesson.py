from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics

from classes.models import Lesson
from classes.serializers.lesson import LessonSerializers
from users.permissions import IsModerator, IsOwner


class LessonDetailView(generics.RetrieveAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializers
    permission_classes = [IsModerator | IsOwner]



class LessonListView(generics.ListAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializers
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ('category', 'in_stock')
    permission_classes = [IsModerator | IsOwner]


class LessonCreateView(generics.CreateAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializers
    permission_classes = [~IsModerator]

    def perform_create(self, serializer):
        new_lesson = serializer.save()
        new_lesson.owner = self.request.user
        new_lesson.save()

class LessonUpdateView(generics.UpdateAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializers
    permission_classes = [IsModerator | IsOwner]


class LessonDeleteView(generics.DestroyAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializers
    permission_classes = [IsOwner]

