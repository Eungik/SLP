from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)


author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'Readingtheeyes'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    eye_practice = models.PositiveIntegerField(initial=None,
                                               choices=[[1, '① Jealous'],
                                                        [2, '② Scared'],
                                                        [3, '③ Relaxed'],
                                                        [4, '④ Hate'],
                                                        ],
                                                verbose_name="",
                                               widget=widgets.RadioSelect())


    eye_q1 = models.PositiveIntegerField(initial=None,
                                      choices=[[1, '① Hate'],
                                               [2, '② Surprised'],
                                               [3, '③ Kind'],
                                               [4, '④ Cross '],
                                               ],
                                      verbose_name="",
                                      widget=widgets.RadioSelect())

    eye_q2 = models.PositiveIntegerField(initial=None,
                                         choices=[[1, '① Unkind'],
                                                  [2, '② Cross'],
                                                  [3, '③ Surprised'],
                                                  [4, '④ Sad '],
                                                  ],
                                         verbose_name="",
                                         widget=widgets.RadioSelect())

    eye_q3 = models.PositiveIntegerField(initial=None,
                                         choices=[[1, '① Friendly'],
                                                  [2, '② Sad'],
                                                  [3, '③ Surprised'],
                                                  [4, '④ Worried'],
                                                  ],
                                         verbose_name="",
                                         widget=widgets.RadioSelect())

    eye_q4 = models.PositiveIntegerField(initial=None,
                                         choices=[[1, '① Relaxed'],
                                                  [2, '② Upset'],
                                                  [3, '③ Surprised'],
                                                  [4, '④ Excited '],
                                                  ],
                                         verbose_name="",
                                         widget=widgets.RadioSelect())

    eye_q5 = models.PositiveIntegerField(initial=None,
                                         choices=[[1, '① Feeling sorry'],
                                                  [2, '② Making somebody do something'],
                                                  [3, '③ Joking'],
                                                  [4, '④ Relaxed'],
                                                  ],
                                         verbose_name="",
                                         widget=widgets.RadioSelect())

    eye_q6 = models.PositiveIntegerField(initial=None,
                                         choices=[[1, '① Hate'],
                                                  [2, '② Unkind'],
                                                  [3, '③ Worried'],
                                                  [4, '④ Bored '],
                                                  ],
                                         verbose_name="",
                                         widget=widgets.RadioSelect())

    eye_q7 = models.PositiveIntegerField(initial=None,
                                         choices=[[1, '① Feeling sorry'],
                                                  [2, '② Bored'],
                                                  [3, '③ Interested'],
                                                  [4, '④ Joking'],
                                                  ],
                                         verbose_name="",
                                         widget=widgets.RadioSelect())

    eye_q8 = models.PositiveIntegerField(initial=None,
                                         choices=[[1, '① Remembering'],
                                                  [2, '② Happy'],
                                                  [3, '③ Friendly'],
                                                  [4, '④ Angry'],
                                                  ],
                                         verbose_name="",
                                         widget=widgets.RadioSelect())

    eye_q9 = models.PositiveIntegerField(initial=None,
                                         choices=[[1, '① Annoyed'],
                                                  [2, '② Hate'],
                                                  [3, '③ Surprised'],
                                                  [4, '④ Thinking about something'],
                                                  ],
                                         verbose_name="",
                                         widget=widgets.RadioSelect())

    eye_q10 = models.PositiveIntegerField(initial=None,
                                         choices=[[1, '① Kind'],
                                                  [2, '② Shy '],
                                                  [3, '③ Not believing'],
                                                  [4, '④ Sad'],
                                                  ],
                                         verbose_name="",
                                         widget=widgets.RadioSelect())

    eye_q11 = models.PositiveIntegerField(initial=None,
                                          choices=[[1, '① Bossy'],
                                                   [2, '② Hoping'],
                                                   [3, '③ Angry'],
                                                   [4, '④ Disgusted'],
                                                   ],
                                          verbose_name="",
                                          widget=widgets.RadioSelect())

    eye_q12 = models.PositiveIntegerField(initial=None,
                                          choices=[[1, '① Confused'],
                                                   [2, '② Joking  '],
                                                   [3, '③ Sad'],
                                                   [4, '④ Serious '],
                                                   ],
                                          verbose_name="",
                                          widget=widgets.RadioSelect())

    eye_q13 = models.PositiveIntegerField(initial=None,
                                          choices=[[1, '① Thinking about something'],
                                                   [2, '② Upset'],
                                                   [3, '③ Excited'],
                                                   [4, '④ Happy'],
                                                   ],
                                          verbose_name="",
                                          widget=widgets.RadioSelect())

    eye_q14 = models.PositiveIntegerField(initial=None,
                                          choices=[[1, '① Happy'],
                                                   [2, '② Thinking about something '],
                                                   [3, '③ Excited'],
                                                   [4, '④ Kind'],
                                                   ],
                                          verbose_name="",
                                          widget=widgets.RadioSelect())

    eye_q15 = models.PositiveIntegerField(initial=None,
                                          choices=[[1, '① Not believing'],
                                                   [2, '② Friendly'],
                                                   [3, '③ Wanting to pay'],
                                                   [4, '④ Relaxed'],
                                                   ],
                                          verbose_name="",
                                          widget=widgets.RadioSelect())

    eye_q16 = models.PositiveIntegerField(initial=None,
                                          choices=[[1, '① Made up her mind'],
                                                   [2, '② Joking'],
                                                   [3, '③ Surprised '],
                                                   [4, '④ Bored'],
                                                   ],
                                          verbose_name="",
                                          widget=widgets.RadioSelect())

    eye_q17 = models.PositiveIntegerField(initial=None,
                                          choices=[[1, '① Angry'],
                                                   [2, '② Friendly '],
                                                   [3, '③ Unkind'],
                                                   [4, '④ A bit worried'],
                                                   ],
                                          verbose_name="",
                                          widget=widgets.RadioSelect())

    eye_q18 = models.PositiveIntegerField(initial=None,
                                          choices=[[1, '① Thinking about something sad'],
                                                   [2, '② Angry'],
                                                   [3, '③ Bossy'],
                                                   [4, '④ Friendly'],
                                                   ],
                                          verbose_name="",
                                          widget=widgets.RadioSelect())

    eye_q19 = models.PositiveIntegerField(initial=None,
                                          choices=[[1, '① Angry'],
                                                   [2, '② Daydreaming'],
                                                   [3, '③ Sad'],
                                                   [4, '④ Interested'],
                                                   ],
                                          verbose_name="",
                                          widget=widgets.RadioSelect())

    eye_q20 = models.PositiveIntegerField(initial=None,
                                          choices=[[1, '① Kind'],
                                                   [2, '② Surprise'],
                                                   [3, '③ Not pleased'],
                                                   [4, '④ Excited'],
                                                   ],
                                          verbose_name="",
                                          widget=widgets.RadioSelect())

    eye_q21 = models.PositiveIntegerField(initial=None,
                                          choices=[[1, '① Interested'],
                                                   [2, '② Joking'],
                                                   [3, '③ Relaxed'],
                                                   [4, '④ Happy'],
                                                   ],
                                          verbose_name="",
                                          widget=widgets.RadioSelect())

    eye_q22 = models.PositiveIntegerField(initial=None,
                                          choices=[[1, '① Playful'],
                                                   [2, '② Kind'],
                                                   [3, '③ Surprised'],
                                                   [4, '④ Thinking about something'],
                                                   ],
                                          verbose_name="",
                                          widget=widgets.RadioSelect())

    eye_q23 = models.PositiveIntegerField(initial=None,
                                          choices=[[1, '① Surprised'],
                                                   [2, '② Sure about something'],
                                                   [3, '③ Joking'],
                                                   [4, '④ Happy'],
                                                   ],
                                          verbose_name="",
                                          widget=widgets.RadioSelect())

    eye_q24 = models.PositiveIntegerField(initial=None,
                                          choices=[[1, '① Serious'],
                                                   [2, '② Ashamed'],
                                                   [3, '③ Confused'],
                                                   [4, '④ Surprised '],
                                                   ],
                                          verbose_name="",
                                          widget=widgets.RadioSelect())

    eye_q25 = models.PositiveIntegerField(initial=None,
                                          choices=[[1, '① Shy'],
                                                   [2, '② Guilty'],
                                                   [3, '③ Daydreaming '],
                                                   [4, '④ Worried'],
                                                   ],
                                          verbose_name="",
                                          widget=widgets.RadioSelect())

    eye_q26 = models.PositiveIntegerField(initial=None,
                                          choices=[[1, '① Joking'],
                                                   [2, '② Relaxed'],
                                                   [3, '③ Nervous'],
                                                   [4, '④ Sorry '],
                                                   ],
                                          verbose_name="",
                                          widget=widgets.RadioSelect())

    eye_q27 = models.PositiveIntegerField(initial=None,
                                          choices=[[1, '① Ashamed'],
                                                   [2, '② Excited '],
                                                   [3, '③ Not believing'],
                                                   [4, '④ Pleased'],
                                                   ],
                                          verbose_name="",
                                          widget=widgets.RadioSelect())

    eye_q28 = models.PositiveIntegerField(initial=None,
                                          choices=[[1, '① Disgust'],
                                                   [2, '② Hate'],
                                                   [3, '③ Happy'],
                                                   [4, '④ Bored'],
                                                   ],
                                          verbose_name="",
                                          widget=widgets.RadioSelect())





