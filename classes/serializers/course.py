from rest_framework import serializers

from classes.models import Course, Lesson
from classes.serializers.lesson import LessonSerializers
from users.models import Subscription


class CourseSerializers(serializers.ModelSerializer):
    quantity_lessons = serializers.SerializerMethodField()
    lessons = LessonSerializers(read_only=True, many=True)

    def get_quantity_lessons(self, obj):
        quantity_lessons = obj.lesson.all().count()

        if not quantity_lessons:
            return None
        else:
            return quantity_lessons

    class Meta:
        model = Course
        fields = '__all__'


class CourseDetailSerializers(serializers.ModelSerializer):
    count_lessons = serializers.SerializerMethodField()
    lessons = LessonSerializers(source='lesson_set', many=True)

    def get_count_lessons(self, course):
        return Lesson.objects.filter(course=course).count()

    class Meta:
        model = Course
        fields = '__all__'


class SubscribeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = '__all__'
