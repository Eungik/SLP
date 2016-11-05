from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)

import random

author = 'Eungik Lee, Master Course Students in SNU'

doc = """
Racegame
"""


class Constants(BaseConstants):
    name_in_url = 'Race'
    players_per_group = None
    num_rounds = 5
    ## Race game N in paper##
    Winning_number=15
    ## Race game k in paper ##
    k=3
    ##
    ## winning reward##
    Winning_reward=20
    ##losing reward##
    Losing_reward=10
    timeout_sec = 6

    winning_set = [p for p in range(1, Winning_number + 1) if (p % (4)) == 3]




class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    Choice=models.PositiveIntegerField(min=1, max=Constants.Winning_number, initial=0)
    computer_choice=models.PositiveIntegerField(initial=0)
    previous_number=models.PositiveIntegerField(initial=0)
    is_winner_15_3=models.PositiveIntegerField(initial=0)
    end = models.PositiveIntegerField(initial=0)

    def ball_statuses(self):
        return [x <= self.previous_number for x in range(1, Constants.Winning_number + 1)]





