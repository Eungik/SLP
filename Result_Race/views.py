from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants

def vars_for_all_templates(self):
    return {
        'rand_num_Rubin' : self.player.participant.vars[Constants.name_in_url]['rand_num_Rubin'],
        'rand_num_Race': self.player.participant.vars[Constants.name_in_url]['rand_num_Race'],
        'high_light' : self.player.participant.vars[Constants.name_in_url]['rand_num_Race']+1,

    }


class Task2_Result(Page):

    def vars_for_template(self):
        return{
            'payoff5_3' : self.participant.vars['is_winner_5_3'],
            'payoff10_3' : self.participant.vars['is_winner_10_3'],
            'payoff15_3' : self.participant.vars['is_winner_15_3'],
            'payoff19_3' : self.participant.vars['is_winner_19_3']

        }

    def before_next_page(self):
        self.player.rand_num_Race=self.player.participant.vars[Constants.name_in_url]['rand_num_Race']

        if self.player.rand_num_Race== 1:
                  self.player.Final_payoff = self.participant.vars['is_winner_5_3'] * 5
                  self.player.lottery_Target = 5

        elif self.player.rand_num_Race == 2:
                self.player.Final_payoff = self.participant.vars['is_winner_10_3'] * 5
                self.player.lottery_Target = 10

        elif self.player.rand_num_Race == 3:
                self.player.Final_payoff = self.participant.vars['is_winner_15_3'] * 5
                self.player.lottery_Target = 15

        elif self.player.rand_num_Race == 4:
            self.player.Final_payoff = self.participant.vars['is_winner_19_3'] * 5
            self.player.lottery_Target = 19


class Task1_Result(Page):

    def before_next_page(self):
        self.player.rand_num_Rubin = self.player.participant.vars[Constants.name_in_url]['rand_num_Rubin']





class Total_Result(Page):

    def vars_for_template(self):
        return{
            'Final_payoff' : self.player.Final_payoff,
            'payoff5_3': self.participant.vars['is_winner_5_3'],
            'payoff10_3': self.participant.vars['is_winner_10_3'],
            'payoff15_3': self.participant.vars['is_winner_15_3'],
            'Showup_added' : self.player.Final_payoff + 5
        }


page_sequence = [
    Task2_Result,
    Task1_Result,
    Total_Result
]
