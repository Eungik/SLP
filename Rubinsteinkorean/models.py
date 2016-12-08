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
    name_in_url = 'Rubinsteinkorean'
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
        choices=[[5,'$5'],[10,'$10'],[15,'$15'],[20,'$20'],[25,'$25'],[30,'$30'],[35,'$35'],[40,'$40'],[45,'$45'],[50,'$50']],
        widget=widgets.RadioSelectHorizontal(),
    )
    Practice1=models.PositiveIntegerField(
        initial=None,
        choices=[[1,'A'],[2,'B'],[3,'C'],[4,'D'],[5,'E']],
        widget=widgets.RadioSelectHorizontal(),
    )
    Practice2=models.CurrencyField(
        initial=None,
    )

    Practice3=models.PositiveIntegerField(
        choices=[[1,'A'],[2,'B'],[3,'C'],[4,'D'],[5,'E']],
        widget=widgets.RadioSelectHorizontal(),
    )
    Practice4=models.CurrencyField(
        initial=None,
    )


    def sequence(self):
        self.Position=self.participant.vars[Constants.name_in_url]['rand_num'][self.round_number-1]




