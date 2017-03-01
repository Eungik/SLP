from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)


author = 'Your name here'

doc = """
Target 10
"""


class Constants(BaseConstants):
    name_in_url = 'Race10_3_Chn'
    players_per_group = None
    num_rounds = 4
    ## Race game N in paper##
    Winning_number=10
    ## Race game k in paper ##
    k=3
    ##
    timeout_sec = 5
    Pseudo_round = 2

    winning_set = [p for p in range(1, Winning_number + 1) if (p % (4)) == 2]


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    Choice=models.PositiveIntegerField(min=1, max=Constants.Winning_number, initial=0)
    computer_choice=models.PositiveIntegerField(initial=0)
    previous_number=models.PositiveIntegerField(initial=0)
    is_winner_10_3=models.PositiveIntegerField(initial=0)
    end = models.PositiveIntegerField(initial=0)
    Pseudo_Round=models.PositiveIntegerField(initial=0)


    def ball_statuses(self):
        return [x <= self.previous_number for x in range(1, Constants.Winning_number + 1)]
