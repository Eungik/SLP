from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants
import random

def vars_for_all_templates(self):
    return {
        'Pseudo_round': Constants.Pseudo_round,
    }



class BasePage(Page):
    def is_displayed(self):
        return sum([p.end for p in self.player.in_all_rounds()]) == 0


class Introduction(Page):

    def is_displayed(self):
        return self.subsession.round_number==1


class MyPage(BasePage):

    form_model=models.Player
    form_fields = ['Choice']

    def vars_for_template(self):
        if self.round_number > 1:
            self.player.previous_number = self.player.in_round(self.round_number - 1).computer_choice
        return {
            'previous_number' : self.player.previous_number,
            'round_number' : self.player.round_number,
            'ball_statuses': self.player.ball_statuses(),
            'ball_numbers': range(1, Constants.Winning_number + 1),
            'end' : self.player.end,
            }



    def before_next_page(self):

        if self.player.Choice in Constants.winning_set:
            random_choice = random.randint(1, Constants.k)
            self.player.computer_choice=self.player.Choice+ random_choice
        else:
            for n in Constants.winning_set:
                if n >  self.player.Choice:
                    self.player.computer_choice = n
                    break




class Computer(BasePage):

    timeout_seconds = Constants.timeout_sec

    def vars_for_template(self):
            return{
                'Choice': self.player.Choice,
                'round_number': self.round_number
             }

    def is_displayed(self):
        return self.player.Choice != Constants.Winning_number and sum([p.end for p in self.player.in_all_rounds()]) == 0


class Win(BasePage):
    def is_displayed(self):
        return self.player.Choice == 10

    def before_next_page(self):
         self.player.end =1
         self.participant.vars['is_winner_10_2'] = 1

    def vars_for_template(self):
        return {
            'Win_num': Constants.Winning_number
        }

class Lose(BasePage):
    def is_displayed(self):
        return 8 <= self.player.Choice < 10

    def before_next_page(self):
        self.player.end = 1
        self.participant.vars['is_winner_10_2'] = 0

    def vars_for_template(self):
        return {
            'Win_num': Constants.Winning_number
        }


page_sequence = [
    Introduction,
    MyPage,
    Computer,
    Win,
    Lose,
]
