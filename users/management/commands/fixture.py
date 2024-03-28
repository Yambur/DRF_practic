from django.core.management import BaseCommand

from classes.models import Course, Lesson
from users.models import Payment, User


class Command(BaseCommand):
    def handle(self, *args, **options):
        users = User.objects.all()
        courses = Course.objects.all()
        lessons = Lesson.objects.all()

        payment_list = []
        if users.exists():
            user = users.first()
            for course in courses:
                payment_list.append(Payment(user=user, course=course, amount="150000", payment_method="перевод"))
            for lesson in lessons[:2]:
                payment_list.append(Payment(user=user, lesson=lesson, amount="10000", payment_method="перевод"))

        Payment.objects.bulk_create(payment_list)