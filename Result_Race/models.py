from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import random

author = 'Eungik'

doc = """
Result Summary
"""


class Constants(BaseConstants):
    name_in_url = 'Result_Race'
    players_per_group = None
    num_rounds = 1
    num_questions=4

class Subsession(BaseSubsession):
    def before_session_starts(self):
        if self.round_number == 1:
            for player in self.get_players():
                player.participant.vars[Constants.name_in_url] = {}
                player.participant.vars[Constants.name_in_url]['rand_num_task2'] = random.randint(1, Constants.num_questions)
                player.participant.vars[Constants.name_in_url]['rand_num_task1'] = random.randint(1, 10)


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    Final_payoff=models.PositiveIntegerField(initial=0)
    rand_num_task2=models.PositiveIntegerField(initial=0)
    rand_num_task1 = models.PositiveIntegerField(initial=0)
    lottery_task2=models.PositiveIntegerField(initial=0)
