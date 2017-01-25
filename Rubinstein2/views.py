from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants




def vars_for_all_templates(self):
    return {
        'rand_num': self.player.participant.vars[Constants.name_in_url]['rand_num'],
        'current' : self.player.participant.vars[Constants.name_in_url]['rand_num'][self.round_number -1],
        'round_number' : self.round_number + 5
    }


class CashPayment(Page):
    def is_displayed(self):
        return self.round_number==1

class Introduction(Page):

    def is_displayed(self):
        return self.round_number==1

    def before_next_page(self):
        self.player.sequence()


class Introduction2(Page):
    def is_displayed(self):
        return self.round_number==1


class Example1(Page):
    def is_displayed(self):
        return self.round_number==1

class Example2(Page):
    def is_displayed(self):
        return self.round_number==1


class Practice(Page):
    form_model=models.Player
    form_fields = ['Practice1_2' , 'Practice2_2']

    def is_displayed(self):
        return self.round_number==1

class Answer(Page):

    def vars_for_template(self):
        return{
            'Practice1_2' : self.player.Practice1_2,
            'Practice2_2' : self.player.Practice2_2
        }

    def is_displayed(self):
        return self.round_number==1

class Practice2(Page):
    form_model=models.Player
    form_fields = ['Practice3_2' , 'Practice4_2']

    def is_displayed(self):
        return self.round_number==1

class Answer2(Page):

    def vars_for_template(self):
        return{
            'Practice3' : self.player.Practice3_2,
            'Practice4' : self.player.Practice4_2
        }

    def is_displayed(self):
        return self.round_number==1

class Question1(Page):
    form_model=models.Player
    form_fields=['Answer_2']

    def before_next_page(self):
        self.player.sequence()






page_sequence = [
    Introduction,
    Introduction2,
    Example1,
    Example2,
    Practice,
    Answer,
    Practice2,
    Answer2,
    Question1,
]
