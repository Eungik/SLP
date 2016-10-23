from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)

import random


author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'Rubinstein'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):

    Page1 = models.PositiveIntegerField(initial=None)
    Page2 = models.PositiveIntegerField(initial=None)
    Page3 = models.PositiveIntegerField(initial=None)
    Page4 = models.PositiveIntegerField(initial=None)
    Page5 = models.PositiveIntegerField(initial=None)

    Rubin_q1=models.PositiveIntegerField(
        initial=None,
        min=11,
        max=20,
    )

    Rubin_q2=models.PositiveIntegerField(
        initial=None,
        min=11,
        max=20,
    )

    Rubin_q3=models.PositiveIntegerField(
        initial=None,
        min=11,
        max=20,
    )

    Rubin_q4=models.PositiveIntegerField(
        initial=None,
        min=11,
        max=20,
    )

    Rubin_q5=models.PositiveIntegerField(
        initial=None,
        min=11,
        max=20,
    )


