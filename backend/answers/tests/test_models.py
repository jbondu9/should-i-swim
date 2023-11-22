from django.test import TestCase

from answers.enums import Reason
from answers.models import Answer


class AnswerTestCase(TestCase):
    def test_create_closed_answer(self):
        answer = Answer(status=Reason.CLOSED.name, description="It's closed!")
        answer.clean()
        answer.save()

        count = Answer.objects.count()

        self.assertGreaterEqual(count, 1)
        self.assertEqual(answer.open, False)

    def test_create_totally_full_answer(self):
        answer = Answer(
            status=Reason.TOTALLY_FULL.name, description="Not now Dude, it's full 😑"
        )
        answer.clean()
        answer.save()

        count = Answer.objects.count()

        self.assertGreaterEqual(count, 1)
        self.assertEqual(answer.open, True)
        self.assertEqual(answer.lower_bound, 80)
        self.assertEqual(answer.upper_bound, 100)
