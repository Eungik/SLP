from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)


author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'IRB4'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    def before_session_starts(self):
        if self.round_number == 1:
            for player in self.get_players():
                player.participant.vars['v'] = 4


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    IRB=models.PositiveIntegerField(initial=None)
    v=models.PositiveIntegerField(initial=None)
