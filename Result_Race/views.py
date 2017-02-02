from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants

def vars_for_all_templates(self):
    return {
        'rand_num_task1' : self.player.participant.vars[Constants.name_in_url]['rand_num_task1'],
        'rand_num': self.player.participant.vars[Constants.name_in_url]['rand_num_task2'],
        'high_light' : self.player.participant.vars[Constants.name_in_url]['rand_num_task2']+1,
        'v': self.player.participant.vars['v']

    }


class Task1_Result(Page):

    def before_next_page(self):
        self.player.rand_num_task1 = self.player.participant.vars[Constants.name_in_url]['rand_num_task1']

class Task2_Result(Page):

    def vars_for_template(self):
        return{
            'payoff5_3' : self.participant.vars['is_winner_5_3'],
            'payoff10_3' : self.participant.vars['is_winner_10_3'],
            'payoff15_3' : self.participant.vars['is_winner_15_3'],

        }

    def before_next_page(self):
        self.player.rand_num_task2=self.player.participant.vars[Constants.name_in_url]['rand_num_task2']

        if  self.player.participant.vars['v'] == 1 :

            if self.player.rand_num_task2== 1:
                  self.player.Final_payoff = self.participant.vars['is_winner_5_3'] * 5
                  self.player.lottery_task2 = 5
            elif self.player.rand_num_task2 == 2:
                  self.player.Final_payoff = self.participant.vars['is_winner_10_3'] * 5
                  self.player.lottery_task2 = 10
            elif self.player.rand_num_task2 == 3:
                  self.player.Final_payoff = self.participant.vars['is_winner_15_3'] * 5
                  self.player.lottery_task2 = 15

        elif self.player.participant.vars['v'] == 2:

            if self.player.rand_num_task2 == 1:
                self.player.Final_payoff = self.participant.vars['is_winner_5_3'] * 5
                self.player.lottery_task2 = 5
            elif self.player.rand_num_task2 == 2:
                self.player.Final_payoff = self.participant.vars['is_winner_15_3'] * 5
                self.player.lottery_task2 = 15
            elif self.player.rand_num_task2 == 3:
                self.player.Final_payoff = self.participant.vars['is_winner_10_3'] * 5
                self.player.lottery_task2 = 10

        elif self.player.participant.vars['v'] == 3:

            if self.player.rand_num_task2 == 1:
                self.player.Final_payoff = self.participant.vars['is_winner_10_3'] * 5
                self.player.lottery_task2 = 10
            elif self.player.rand_num_task2 == 2:
                self.player.Final_payoff = self.participant.vars['is_winner_5_3'] * 5
                self.player.lottery_task2 = 5
            elif self.player.rand_num_task2 == 3:
                self.player.Final_payoff = self.participant.vars['is_winner_15_3'] * 5
                self.player.lottery_task2 = 15

        elif self.player.participant.vars['v'] == 4:

            if self.player.rand_num_task2 == 1:
                self.player.Final_payoff = self.participant.vars['is_winner_10_3'] * 5
                self.player.lottery_task2 = 10
            elif self.player.rand_num_task2 == 2:
                self.player.Final_payoff = self.participant.vars['is_winner_15_3'] * 5
                self.player.lottery_task2 = 15
            elif self.player.rand_num_task2 == 3:
                self.player.Final_payoff = self.participant.vars['is_winner_5_3'] * 5
                self.player.lottery_task2 = 5

        elif self.player.participant.vars['v'] == 5:

            if self.player.rand_num_task2 == 1:
                self.player.Final_payoff = self.participant.vars['is_winner_15_3'] * 5
                self.player.lottery_task2 = 15
            elif self.player.rand_num_task2 == 2:
                self.player.Final_payoff = self.participant.vars['is_winner_5_3'] * 5
                self.player.lottery_task2 = 5
            elif self.player.rand_num_task2 == 3:
                self.player.Final_payoff = self.participant.vars['is_winner_10_3'] * 5
                self.player.lottery_task2 = 10

        elif self.player.participant.vars['v'] == 6:

            if self.player.rand_num_task2 == 1:
                self.player.Final_payoff = self.participant.vars['is_winner_15_3'] * 5
                self.player.lottery_task2 = 15
            elif self.player.rand_num_task2 == 2:
                self.player.Final_payoff = self.participant.vars['is_winner_10_3'] * 5
                self.player.lottery_task2 = 10
            elif self.player.rand_num_task2 == 3:
                self.player.Final_payoff = self.participant.vars['is_winner_5_3'] * 5
                self.player.lottery_task2 = 5

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
    Task1_Result,
    Task2_Result,
    Total_Result
]
