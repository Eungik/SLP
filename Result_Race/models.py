from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)


author = 'Eungik'

doc = """
Result Summary
"""


class Constants(BaseConstants):
    name_in_url = 'Result_Race'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    Final_payoff=models.PositiveIntegerField(initial=0)
