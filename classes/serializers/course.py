from rest_framework import serializers

from classes.models import Course, Lesson


class CourseSerializers(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'


class CourseDetailSerializers(serializers.ModelSerializer):
    count_lessons = serializers.SerializerMethodField()

    def get_count_lessons(self, course):
        return Lesson.objects.filter(course=course).count()

    class Meta:
        model = Course
        fields = '__all__'
