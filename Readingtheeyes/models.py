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
    eye_q1 = models.PositiveIntegerField(initial=None,
                                      choices=[[1, '① Playful'],
                                               [2, '② Comforting'],
                                               [3, '③ Irritated'],
                                               [4, '④ Bored '],
                                               ],
                                      verbose_name="",
                                      widget=widgets.RadioSelect())

    eye_q2 = models.PositiveIntegerField(initial=None,
                                         choices=[[1, '① Arrogant'],
                                                  [2, '② Annoyed'],
                                                  [3, '③ Upset'],
                                                  [4, '④ Terrified '],
                                                  ],
                                         verbose_name="",
                                         widget=widgets.RadioSelect())

    eye_q3 = models.PositiveIntegerField(initial=None,
                                         choices=[[1, '① Convinced'],
                                                  [2, '② Flustered'],
                                                  [3, '③ Desire'],
                                                  [4, '④ Joking '],
                                                  ],
                                         verbose_name="",
                                         widget=widgets.RadioSelect())

    eye_q4 = models.PositiveIntegerField(initial=None,
                                         choices=[[1, '① Amused'],
                                                  [2, '② Relaxed'],
                                                  [3, '③ Joking'],
                                                  [4, '④ Insisting '],
                                                  ],
                                         verbose_name="",
                                         widget=widgets.RadioSelect())

    eye_q5 = models.PositiveIntegerField(initial=None,
                                         choices=[[1, '① Friendly'],
                                                  [2, '② Irritated'],
                                                  [3, '③ Worried'],
                                                  [4, '④ Sarcastic '],
                                                  ],
                                         verbose_name="",
                                         widget=widgets.RadioSelect())

    eye_q6 = models.PositiveIntegerField(initial=None,
                                         choices=[[1, '① Fantasizing'],
                                                  [2, '② Alarmed'],
                                                  [3, '③ Aghast'],
                                                  [4, '④ Impatient '],
                                                  ],
                                         verbose_name="",
                                         widget=widgets.RadioSelect())

    eye_q7 = models.PositiveIntegerField(initial=None,
                                         choices=[[1, '① Uneasy'],
                                                  [2, '② Friendly'],
                                                  [3, '③ Apologetic'],
                                                  [4, '④ Dispirited'],
                                                  ],
                                         verbose_name="",
                                         widget=widgets.RadioSelect())

    eye_q8 = models.PositiveIntegerField(initial=None,
                                         choices=[[1, '① Excited'],
                                                  [2, '② Relieved'],
                                                  [3, '③ Shy'],
                                                  [4, '④ Despondent'],
                                                  ],
                                         verbose_name="",
                                         widget=widgets.RadioSelect())

    eye_q9 = models.PositiveIntegerField(initial=None,
                                         choices=[[1, '① Annoyed'],
                                                  [2, '② Hostile'],
                                                  [3, '③ Horrified'],
                                                  [4, '④ Preoccupied'],
                                                  ],
                                         verbose_name="",
                                         widget=widgets.RadioSelect())

    eye_q10 = models.PositiveIntegerField(initial=None,
                                         choices=[[1, '① Cautious'],
                                                  [2, '② Bored '],
                                                  [3, '③ Aghast'],
                                                  [4, '④ Insisting'],
                                                  ],
                                         verbose_name="",
                                         widget=widgets.RadioSelect())

    eye_q11 = models.PositiveIntegerField(initial=None,
                                          choices=[[1, '① Terrified'],
                                                   [2, '② Flirtatious '],
                                                   [3, '③ Amused'],
                                                   [4, '④ Regretful'],
                                                   ],
                                          verbose_name="",
                                          widget=widgets.RadioSelect())

    eye_q12 = models.PositiveIntegerField(initial=None,
                                          choices=[[1, '① Skeptical'],
                                                   [2, '② Embarrassed  '],
                                                   [3, '③ Dispirited'],
                                                   [4, '④ Indifferent '],
                                                   ],
                                          verbose_name="",
                                          widget=widgets.RadioSelect())

    eye_q13 = models.PositiveIntegerField(initial=None,
                                          choices=[[1, '① Shy'],
                                                   [2, '② Decisive'],
                                                   [3, '③ Threatening'],
                                                   [4, '④ Anticipating'],
                                                   ],
                                          verbose_name="",
                                          widget=widgets.RadioSelect())

    eye_q14 = models.PositiveIntegerField(initial=None,
                                          choices=[[1, '① Irritated'],
                                                   [2, '② Disappointed '],
                                                   [3, '③ Depressed'],
                                                   [4, '④ Accusing'],
                                                   ],
                                          verbose_name="",
                                          widget=widgets.RadioSelect())

    eye_q15 = models.PositiveIntegerField(initial=None,
                                          choices=[[1, '① Encouraging'],
                                                   [2, '② Amused'],
                                                   [3, '③ Flustered'],
                                                   [4, '④ Contemplative'],
                                                   ],
                                          verbose_name="",
                                          widget=widgets.RadioSelect())

    eye_q16 = models.PositiveIntegerField(initial=None,
                                          choices=[[1, '① Thoughtful'],
                                                   [2, '② Irritated'],
                                                   [3, '③ Encouraging '],
                                                   [4, '④ Sympathetic'],
                                                   ],
                                          verbose_name="",
                                          widget=widgets.RadioSelect())

    eye_q17 = models.PositiveIntegerField(initial=None,
                                          choices=[[1, '① Playful'],
                                                   [2, '② Affectionate '],
                                                   [3, '③ Aghast'],
                                                   [4, '④ Doubtful'],
                                                   ],
                                          verbose_name="",
                                          widget=widgets.RadioSelect())

    eye_q18 = models.PositiveIntegerField(initial=None,
                                          choices=[[1, '① Amused'],
                                                   [2, '② Bored '],
                                                   [3, '③ Decisive '],
                                                   [4, '④ Aghast '],
                                                   ],
                                          verbose_name="",
                                          widget=widgets.RadioSelect())

    eye_q19 = models.PositiveIntegerField(initial=None,
                                          choices=[[1, '① Arrogant'],
                                                   [2, '② Grateful'],
                                                   [3, '③ Tentative'],
                                                   [4, '④ Sarcastic'],
                                                   ],
                                          verbose_name="",
                                          widget=widgets.RadioSelect())

    eye_q20 = models.PositiveIntegerField(initial=None,
                                          choices=[[1, '① Friendly'],
                                                   [2, '② Horrified'],
                                                   [3, '③ Guilty '],
                                                   [4, '④ Dominant '],
                                                   ],
                                          verbose_name="",
                                          widget=widgets.RadioSelect())

    eye_q21 = models.PositiveIntegerField(initial=None,
                                          choices=[[1, '① Panicked'],
                                                   [2, '② Fantasizing'],
                                                   [3, '③ Confused'],
                                                   [4, '④ Embarrassed '],
                                                   ],
                                          verbose_name="",
                                          widget=widgets.RadioSelect())

    eye_q22 = models.PositiveIntegerField(initial=None,
                                          choices=[[1, '① Preoccupied'],
                                                   [2, '② Insisting '],
                                                   [3, '③ Imploring '],
                                                   [4, '④ Grateful'],
                                                   ],
                                          verbose_name="",
                                          widget=widgets.RadioSelect())

    eye_q23 = models.PositiveIntegerField(initial=None,
                                          choices=[[1, '① Curious'],
                                                   [2, '② Apologetic '],
                                                   [3, '③ Contented'],
                                                   [4, '④ Defiant'],
                                                   ],
                                          verbose_name="",
                                          widget=widgets.RadioSelect())

    eye_q24 = models.PositiveIntegerField(initial=None,
                                          choices=[[1, '① Pensive'],
                                                   [2, '② Irritated'],
                                                   [3, '③ Excited'],
                                                   [4, '④ Hostile '],
                                                   ],
                                          verbose_name="",
                                          widget=widgets.RadioSelect())

    eye_q25 = models.PositiveIntegerField(initial=None,
                                          choices=[[1, '① Incredulous'],
                                                   [2, '② Panicked'],
                                                   [3, '③ Interested '],
                                                   [4, '④ Despondent'],
                                                   ],
                                          verbose_name="",
                                          widget=widgets.RadioSelect())

    eye_q26 = models.PositiveIntegerField(initial=None,
                                          choices=[[1, '① Alarmed'],
                                                   [2, '② Anxious'],
                                                   [3, '③ Shy'],
                                                   [4, '④ Hostile '],
                                                   ],
                                          verbose_name="",
                                          widget=widgets.RadioSelect())

    eye_q27 = models.PositiveIntegerField(initial=None,
                                          choices=[[1, '① Arrogant'],
                                                   [2, '② Cautious '],
                                                   [3, '③ Reassuring'],
                                                   [4, '④ Joking '],
                                                   ],
                                          verbose_name="",
                                          widget=widgets.RadioSelect())

    eye_q28 = models.PositiveIntegerField(initial=None,
                                          choices=[[1, '① Affectionate'],
                                                   [2, '② Joking'],
                                                   [3, '③ Interested'],
                                                   [4, '④ Contented '],
                                                   ],
                                          verbose_name="",
                                          widget=widgets.RadioSelect())

    eye_q29 = models.PositiveIntegerField(initial=None,
                                          choices=[[1, '① Impatient '],
                                                   [2, '② Aghast'],
                                                   [3, '③ Irritated'],
                                                   [4, '④ Reflective'],
                                                   ],
                                          verbose_name="",
                                          widget=widgets.RadioSelect())

    eye_q30 = models.PositiveIntegerField(initial=None,
                                          choices=[[1, '① Flirtatious'],
                                                   [2, '② Disappointed'],
                                                   [3, '③ Hostile'],
                                                   [4, '④ Grateful'],
                                                   ],
                                          verbose_name="",
                                          widget=widgets.RadioSelect())

    eye_q31 = models.PositiveIntegerField(initial=None,
                                          choices=[[1, '① Joking'],
                                                   [2, '② Ashamed'],
                                                   [3, '③ Confident'],
                                                   [4, '④ Dispirited '],
                                                   ],
                                          verbose_name="",
                                          widget=widgets.RadioSelect())

    eye_q32 = models.PositiveIntegerField(initial=None,
                                          choices=[[1, '① Ashamed'],
                                                   [2, '② Bewildered'],
                                                   [3, '③ Alarmed'],
                                                   [4, '④ Serious'],
                                                   ],
                                          verbose_name="",
                                          widget=widgets.RadioSelect())

    eye_q33 = models.PositiveIntegerField(initial=None,
                                          choices=[[1, '① Concerned'],
                                                   [2, '② Embarrassed'],
                                                   [3, '③ Guilty'],
                                                   [4, '④ Fantasizing'],
                                                   ],
                                          verbose_name="",
                                          widget=widgets.RadioSelect())

    eye_q34 = models.PositiveIntegerField(initial=None,
                                          choices=[[1, '① Aghast'],
                                                   [2, '② Baffled'],
                                                   [3, '③ Terrified'],
                                                   [4, '④ Distrustful'],
                                                   ],
                                          verbose_name="",
                                          widget=widgets.RadioSelect())

    eye_q35 = models.PositiveIntegerField(initial=None,
                                          choices=[[1, '① Nervous'],
                                                   [2, '② Contemplative'],
                                                   [3, '③ Insisting'],
                                                   [4, '④ Puzzled'],
                                                   ],
                                          verbose_name="",
                                          widget=widgets.RadioSelect())

    eye_q36 = models.PositiveIntegerField(initial=None,
                                          choices=[[1, '① Suspicious'],
                                                   [2, '② Nervous'],
                                                   [3, '③ Ashamed'],
                                                   [4, '④ Indecisive'],
                                                   ],
                                          verbose_name="",
                                          widget=widgets.RadioSelect())




