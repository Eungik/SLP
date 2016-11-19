from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants


class Introduction(Page):
    def is_displayed(self):
        return self.round_number == 1

class Sample_intro(Page):
    def is_displayed(self):
        return self.round_number == 1

class Sample1(Page):
    def is_displayed(self):
        return self.round_number == 1

class Sample2(Page):
    def is_displayed(self):
        return self.round_number == 1

class Sample3(Page):
    def is_displayed(self):
        return self.round_number == 1





page_sequence = [
    Introduction,
    Sample_intro,
    Sample1,
    Sample2,
]
