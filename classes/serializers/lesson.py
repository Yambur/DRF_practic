from rest_framework import serializers
from rest_framework.relations import SlugRelatedField

from classes.models import Lesson, Course
from classes.validators import LinkValidator


class LessonSerializers(serializers.ModelSerializer):
    validators = [LinkValidator(field='link_video')]

    class Meta:
        model = Lesson
        fields = '__all__'


class LessonListSerializer(serializers.ModelSerializer):
    course = SlugRelatedField(slug_field='title', queryset=Course.objects.all())

    class Meta:
        model = Lesson
        fields = ('title', 'course',)


class LessonDetailSerializer(serializers.ModelSerializer):
    course = SlugRelatedField(slug_field='title', queryset=Course.objects.all())

    class Meta:
        model = Lesson
        fields = '__all__'
