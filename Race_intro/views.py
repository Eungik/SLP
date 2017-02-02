from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants

def vars_for_all_templates(self):
    return {
        'Pseudo_Round': self.player.participant.vars['Race_intro']['Pseudo_Round']
    }


class Introduction(Page):
    def is_displayed(self):
        return self.round_number == 1

class Introduction2(Page):
    def is_displayed(self):
        return self.round_number == 1



class Sample_intro(Page):
    def is_displayed(self):
        return self.round_number == 1

class Sample1(Page):

    form_model=models.Player
    form_fields = ['Practice']

    def is_displayed(self):
        return self.round_number == 1

class Sample2(Page):
    def is_displayed(self):
        return self.round_number == 1

    def vars_for_template(self):
        return{
            'practice': self.player.Practice
        }

class Sample3(Page):
    def is_displayed(self):
        return self.round_number == 1

    def before_next_page(self):
        self.player.participant.vars['Race_intro']['Pseudo_Round'] += 1






page_sequence = [
    Introduction,
    Introduction2,
    Sample_intro,
    Sample1,
    Sample2,
    Sample3,
]
