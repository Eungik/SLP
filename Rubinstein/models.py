import random


from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)




author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'Rubinstein'
    players_per_group = None
    num_rounds = 5


class Subsession(BaseSubsession):

    def before_session_starts(self):
        if self.round_number == 1:
            for player in self.get_players():
                    player.participant.vars[Constants.name_in_url] = {}
                    player.participant.vars[Constants.name_in_url]['rand_num'] = random.sample([1,2,3,4,5],5)



class Group(BaseGroup):
    pass


class Player(BasePlayer):

    Position=models.PositiveIntegerField()

    Answer=models.PositiveIntegerField(
        initial=None,
        min=11,
        max=20,
    )


    def set_payoff(self):
        self.Position=self.participant.vars[Constants.name_in_url]['rand_num'][self.round_number-1]




