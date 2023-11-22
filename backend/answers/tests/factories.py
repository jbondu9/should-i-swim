from factory.django import DjangoModelFactory
from factory.fuzzy import FuzzyChoice
from factory import Faker, post_generation

from answers.enums import Reason
from answers.models import Answer
from answers.utils import get_lower_bound, get_open, get_upper_bound


class AnswerFactory(DjangoModelFactory):
    class Meta:
        model = Answer

    status = FuzzyChoice(Answer.REASON_CHOICES, getter=lambda c: c[0])
    description = Faker("paragraph", nb_sentences=1)

    @post_generation
    def clean(self, create, extracted, **kwargs):
        if not create:
            return
        self.open = get_open(self.status)
        self.lower_bound = get_lower_bound(self.status)
        self.upper_bound = get_upper_bound(self.status)
