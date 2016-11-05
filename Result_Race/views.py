from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants


class MyPage(Page):

    def vars_for_template(self):
        return{
            'payoff4_2' : self.participant.vars['is_winner_4_2'],
            'payoff6_3' : self.participant.vars['is_winner_6_3'],
            'payoff8_2' : self.participant.vars['is_winner_8_2'],
            'payoff11_3' : self.participant.vars['is_winner_11_3'],
            'payoff10_2' : self.participant.vars['is_winner_10_2'],
            'payoff15_3' : self.participant.vars['is_winner_15_3']

        }


class ResultsWaitPage(WaitPage):

    def after_all_players_arrive(self):
        pass


class Results(Page):
    pass


page_sequence = [
    MyPage,

    Results
]
