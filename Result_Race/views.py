from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants

def vars_for_all_templates(self):
    return {
        'rand_num': self.player.participant.vars[Constants.name_in_url]['rand_num'],
        'high_light' : self.player.participant.vars[Constants.name_in_url]['rand_num']+1
    }




class MyPage(Page):

    def vars_for_template(self):
        return{
            'payoff4_2' : self.participant.vars['is_winner_4_2'],
            'payoff6_3' : self.participant.vars['is_winner_6_3'],
            'payoff8_2' : self.participant.vars['is_winner_8_2'],
            'payoff11_3' : self.participant.vars['is_winner_11_3'],
            'payoff10_2' : self.participant.vars['is_winner_10_2'],
            'payoff15_3' : self.participant.vars['is_winner_15_3'],

        }

    def before_next_page(self):
        self.player.rand_num=self.player.participant.vars[Constants.name_in_url]['rand_num']
        if self.player.rand_num == 1:
            self.player.Final_payoff = self.participant.vars['is_winner_4_2'] * 5
        elif self.player.rand_num == 2:
            self.player.Final_payoff = self.participant.vars['is_winner_6_3'] * 5
        elif self.player.rand_num == 3:
            self.player.Final_payoff = self.participant.vars['is_winner_8_2'] * 5
        elif self.player.rand_num == 4:
            self.player.Final_payoff = self.participant.vars['is_winner_11_3'] * 5
        elif self.player.rand_num == 5:
            self.player.Final_payoff = self.participant.vars['is_winner_10_2'] * 5
        elif self.player.rand_num == 6:
            self.player.Final_payoff = self.participant.vars['is_winner_15_3'] * 5


class Results(Page):
    def vars_for_template(self):
        return{
            'Final_payoff' : self.player.Final_payoff
        }


page_sequence = [
    MyPage,
    Results
]
