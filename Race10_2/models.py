from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)


author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'Race10_2'
    players_per_group = None
    num_rounds = 10
    ## Race game N in paper##
    Winning_number=10
    ## Race game k in paper ##
    k=2
    ##
    ## winning reward##
    Winning_reward=20
    ##losing reward##
    Losing_reward=10
    timeout_sec = 6
    Pseudo_round = 5

    winning_set = [p for p in range(1, Winning_number + 1) if (p % (3)) == 1]


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    Choice=models.PositiveIntegerField(min=1, max=Constants.Winning_number, initial=0)
    computer_choice=models.PositiveIntegerField(initial=0)
    previous_number=models.PositiveIntegerField(initial=0)
    is_winner_4_2=models.PositiveIntegerField(initial=0)
    end = models.PositiveIntegerField(initial=0)


    def ball_statuses(self):
        return [x <= self.previous_number for x in range(1, Constants.Winning_number + 1)]
