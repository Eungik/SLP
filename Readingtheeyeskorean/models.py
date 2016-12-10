from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)


author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'Readingtheeyeskorean'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    eye_practice = models.PositiveIntegerField(initial=None,
                                               choices=[[1, '① 질투'],
                                                        [2, '② 무서움'],
                                                        [3, '③ 안정'],
                                                        [4, '④ 미움'],
                                                        ],
                                                verbose_name="",
                                               widget=widgets.RadioSelect())


    eye_q1 = models.PositiveIntegerField(initial=None,
                                      choices=[[1, '① 증오'],
                                               [2, '② 놀람'],
                                               [3, '③ 친절함'],
                                               [4, '④ 두려움'],
                                               ],
                                      verbose_name="",
                                      widget=widgets.RadioSelect())






