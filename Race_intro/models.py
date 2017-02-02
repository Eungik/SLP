from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)


author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'Race_intro'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    def before_session_starts(self):
        if self.round_number == 1:
            for player in self.get_players():
                player.participant.vars[Constants.name_in_url] = {}
                player.participant.vars[Constants.name_in_url]['Pseudo_Round'] = 0


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    Practice = models.PositiveIntegerField(min=1, max=3, initial=0)
    Pseudo_Round=models.PositiveIntegerField(initial=0)

