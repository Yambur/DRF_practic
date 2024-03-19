from django.core.management import BaseCommand

from classes.models import Course, Lesson
from users.models import Payment, User


class Command(BaseCommand):
    def handle(self, *args, **options):
        users = User.objects.all()
        courses = Course.objects.all()
        lessons = Lesson.objects.all()

        payment_list = [
            {"user": users[0], "course": courses[0], "amount": "150000", "payment_method": "перевод"},
            {"user": users[0], "lesson": lessons[1], "amount": "10000", "payment_method": "перевод"},
        ]

        payments_for_create = []
        for payment in payment_list:
            payments_for_create.append(Payment(**payment))
        Payment.objects.bulk_create(payments_for_create)
