from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants




def vars_for_all_templates(self):
    return {
        'rand_num': self.player.participant.vars[Constants.name_in_url]['rand_num'],
        'current' : self.player.participant.vars[Constants.name_in_url]['rand_num'][self.round_number -1]
    }


class Introduction(Page):

    def is_displayed(self):
        return self.round_number==1

    def before_next_page(self):
        self.player.set_payoff()

class Question1(Page):
    form_model=models.Player
    form_fields=['Answer']

    def before_next_page(self):
        self.player.set_payoff()




page_sequence = [
    Introduction,
    Question1,
]