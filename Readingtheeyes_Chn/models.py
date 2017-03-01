from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)


author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'Readingtheeyes_Chn'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    eye_practice = models.PositiveIntegerField(initial=None,
                                               choices=[[1, '① 嫉妒的'],
                                                        [2, '② 恐惧的'],
                                                        [3, '③ 放松的'],
                                                        [4, '④ 增恨'],
                                                        ],
                                                verbose_name="",
                                               widget=widgets.RadioSelect())


    eye_q1 = models.PositiveIntegerField(initial=None,
                                      choices=[[1, '① 增恨'],
                                               [2, '② 令人惊讶的'],
                                               [3, '③ 善良的'],
                                               [4, '④ 作对 '],
                                               ],
                                      verbose_name="",
                                      widget=widgets.RadioSelect())

    eye_q2 = models.PositiveIntegerField(initial=None,
                                         choices=[[1, '① 不厚道的'],
                                                  [2, '② 作对'],
                                                  [3, '③ 令人惊讶的'],
                                                  [4, '④ 悲伤的 '],
                                                  ],
                                         verbose_name="",
                                         widget=widgets.RadioSelect())

    eye_q3 = models.PositiveIntegerField(initial=None,
                                         choices=[[1, '① 友好的'],
                                                  [2, '② 悲伤的'],
                                                  [3, '③ 令人惊讶的'],
                                                  [4, '④ 焦虑的'],
                                                  ],
                                         verbose_name="",
                                         widget=widgets.RadioSelect())

    eye_q4 = models.PositiveIntegerField(initial=None,
                                         choices=[[1, '① 放松的'],
                                                  [2, '② 不安的'],
                                                  [3, '③ 令人惊讶的'],
                                                  [4, '④ 兴奋的 '],
                                                  ],
                                         verbose_name="",
                                         widget=widgets.RadioSelect())

    eye_q5 = models.PositiveIntegerField(initial=None,
                                         choices=[[1, '① 感觉抱歉'],
                                                  [2, '② 让某人做某事'],
                                                  [3, '③ 开玩笑的'],
                                                  [4, '④ 放松的'],
                                                  ],
                                         verbose_name="",
                                         widget=widgets.RadioSelect())

    eye_q6 = models.PositiveIntegerField(initial=None,
                                         choices=[[1, '① 增恨'],
                                                  [2, '② 不厚道的'],
                                                  [3, '③ 焦虑的'],
                                                  [4, '④ 无聊的'],
                                                  ],
                                         verbose_name="",
                                         widget=widgets.RadioSelect())

    eye_q7 = models.PositiveIntegerField(initial=None,
                                         choices=[[1, '① 感觉抱歉'],
                                                  [2, '② 无聊的'],
                                                  [3, '③ 感兴趣的'],
                                                  [4, '④ 开玩笑的'],
                                                  ],
                                         verbose_name="",
                                         widget=widgets.RadioSelect())

    eye_q8 = models.PositiveIntegerField(initial=None,
                                         choices=[[1, '① 记得'],
                                                  [2, '② 快乐的'],
                                                  [3, '③ 友好的'],
                                                  [4, '④ 生气的'],
                                                  ],
                                         verbose_name="",
                                         widget=widgets.RadioSelect())

    eye_q9 = models.PositiveIntegerField(initial=None,
                                         choices=[[1, '① 烦人的'],
                                                  [2, '② 增恨'],
                                                  [3, '③ 令人惊讶的'],
                                                  [4, '④ 思考某事'],
                                                  ],
                                         verbose_name="",
                                         widget=widgets.RadioSelect())

    eye_q10 = models.PositiveIntegerField(initial=None,
                                         choices=[[1, '① 善良的'],
                                                  [2, '② 害羞的 '],
                                                  [3, '③ 不相信'],
                                                  [4, '④ 悲伤的'],
                                                  ],
                                         verbose_name="",
                                         widget=widgets.RadioSelect())

    eye_q11 = models.PositiveIntegerField(initial=None,
                                          choices=[[1, '① 专横的'],
                                                   [2, '② 希望'],
                                                   [3, '③ 生气的'],
                                                   [4, '④ 厌恶的'],
                                                   ],
                                          verbose_name="",
                                          widget=widgets.RadioSelect())

    eye_q12 = models.PositiveIntegerField(initial=None,
                                          choices=[[1, '① 迷惑的'],
                                                   [2, '② 开玩笑的  '],
                                                   [3, '③ 悲伤的'],
                                                   [4, '④ 认真的 '],
                                                   ],
                                          verbose_name="",
                                          widget=widgets.RadioSelect())

    eye_q13 = models.PositiveIntegerField(initial=None,
                                          choices=[[1, '① 思考某事'],
                                                   [2, '② 不安的'],
                                                   [3, '③ 兴奋的'],
                                                   [4, '④ 快乐的'],
                                                   ],
                                          verbose_name="",
                                          widget=widgets.RadioSelect())

    eye_q14 = models.PositiveIntegerField(initial=None,
                                          choices=[[1, '① 快乐的'],
                                                   [2, '② 思考某事'],
                                                   [3, '③ 兴奋的'],
                                                   [4, '④ 善良的'],
                                                   ],
                                          verbose_name="",
                                          widget=widgets.RadioSelect())

    eye_q15 = models.PositiveIntegerField(initial=None,
                                          choices=[[1, '① 不相信'],
                                                   [2, '② 友好的'],
                                                   [3, '③ 想要玩耍'],
                                                   [4, '④ 放松的'],
                                                   ],
                                          verbose_name="",
                                          widget=widgets.RadioSelect())

    eye_q16 = models.PositiveIntegerField(initial=None,
                                          choices=[[1, '① 下决心'],
                                                   [2, '② 开玩笑的'],
                                                   [3, '③ 吃惊的'],
                                                   [4, '④ 无聊的'],
                                                   ],
                                          verbose_name="",
                                          widget=widgets.RadioSelect())

    eye_q17 = models.PositiveIntegerField(initial=None,
                                          choices=[[1, '① 生气的'],
                                                   [2, '② 友好的'],
                                                   [3, '③ 不厚道的'],
                                                   [4, '④ 有些焦虑的'],
                                                   ],
                                          verbose_name="",
                                          widget=widgets.RadioSelect())

    eye_q18 = models.PositiveIntegerField(initial=None,
                                          choices=[[1, '① 思考某些伤心的事'],
                                                   [2, '② 生气的'],
                                                   [3, '③ 专横的'],
                                                   [4, '④ 友好的'],
                                                   ],
                                          verbose_name="",
                                          widget=widgets.RadioSelect())

    eye_q19 = models.PositiveIntegerField(initial=None,
                                          choices=[[1, '① 生气的'],
                                                   [2, '② 做白日梦'],
                                                   [3, '③ 悲伤的'],
                                                   [4, '④ 感兴趣的'],
                                                   ],
                                          verbose_name="",
                                          widget=widgets.RadioSelect())

    eye_q20 = models.PositiveIntegerField(initial=None,
                                          choices=[[1, '① 善良的'],
                                                   [2, '② 令人惊讶的'],
                                                   [3, '③ 不愉悦的'],
                                                   [4, '④ 兴奋的'],
                                                   ],
                                          verbose_name="",
                                          widget=widgets.RadioSelect())

    eye_q21 = models.PositiveIntegerField(initial=None,
                                          choices=[[1, '① 感兴趣的'],
                                                   [2, '② 开玩笑的'],
                                                   [3, '③ 放松的'],
                                                   [4, '④ 快乐的'],
                                                   ],
                                          verbose_name="",
                                          widget=widgets.RadioSelect())

    eye_q22 = models.PositiveIntegerField(initial=None,
                                          choices=[[1, '① 顽皮的'],
                                                   [2, '② 善良的'],
                                                   [3, '③ 吃惊的'],
                                                   [4, '④ 思考某事'],
                                                   ],
                                          verbose_name="",
                                          widget=widgets.RadioSelect())

    eye_q23 = models.PositiveIntegerField(initial=None,
                                          choices=[[1, '① 吃惊的'],
                                                   [2, '② 确信某事'],
                                                   [3, '③ 开玩笑的'],
                                                   [4, '④ 快乐的'],
                                                   ],
                                          verbose_name="",
                                          widget=widgets.RadioSelect())

    eye_q24 = models.PositiveIntegerField(initial=None,
                                          choices=[[1, '① 认真的'],
                                                   [2, '② 羞愧的'],
                                                   [3, '③ 迷惑的'],
                                                   [4, '④ 吃惊的'],
                                                   ],
                                          verbose_name="",
                                          widget=widgets.RadioSelect())

    eye_q25 = models.PositiveIntegerField(initial=None,
                                          choices=[[1, '① 害羞的'],
                                                   [2, '② 内疚的'],
                                                   [3, '③ 做白日梦 '],
                                                   [4, '④ 焦虑的'],
                                                   ],
                                          verbose_name="",
                                          widget=widgets.RadioSelect())

    eye_q26 = models.PositiveIntegerField(initial=None,
                                          choices=[[1, '① 开玩笑的'],
                                                   [2, '② 放松的'],
                                                   [3, '③ 紧张的'],
                                                   [4, '④ 抱歉的 '],
                                                   ],
                                          verbose_name="",
                                          widget=widgets.RadioSelect())

    eye_q27 = models.PositiveIntegerField(initial=None,
                                          choices=[[1, '① 羞愧的'],
                                                   [2, '② 兴奋的'],
                                                   [3, '③ 不相信'],
                                                   [4, '④ 愉悦的'],
                                                   ],
                                          verbose_name="",
                                          widget=widgets.RadioSelect())

    eye_q28 = models.PositiveIntegerField(initial=None,
                                          choices=[[1, '① 作呕'],
                                                   [2, '② 增恨'],
                                                   [3, '③ 快乐的'],
                                                   [4, '④ 无聊'],
                                                   ],
                                          verbose_name="",
                                          widget=widgets.RadioSelect())

    correct0 = models.IntegerField(initial=0)
    correct1 = models.IntegerField(initial=0)
    correct2 = models.IntegerField(initial=0)
    correct3 = models.IntegerField(initial=0)
    correct4 = models.IntegerField(initial=0)
    correct5 = models.IntegerField(initial=0)
    correct6 = models.IntegerField(initial=0)
    correct7 = models.IntegerField(initial=0)
    correct8 = models.IntegerField(initial=0)
    correct9 = models.IntegerField(initial=0)
    correct10 = models.IntegerField(initial=0)
    correct11 = models.IntegerField(initial=0)
    correct12 = models.IntegerField(initial=0)
    correct13 = models.IntegerField(initial=0)
    correct14 = models.IntegerField(initial=0)
    correct15 = models.IntegerField(initial=0)
    correct16 = models.IntegerField(initial=0)
    correct17 = models.IntegerField(initial=0)
    correct18 = models.IntegerField(initial=0)
    correct19 = models.IntegerField(initial=0)
    correct20 = models.IntegerField(initial=0)
    correct21 = models.IntegerField(initial=0)
    correct22 = models.IntegerField(initial=0)
    correct23 = models.IntegerField(initial=0)
    correct24 = models.IntegerField(initial=0)
    correct25 = models.IntegerField(initial=0)
    correct26 = models.IntegerField(initial=0)
    correct27 = models.IntegerField(initial=0)
    correct28 = models.IntegerField(initial=0)
    correct_total=models.IntegerField(initial=0)






