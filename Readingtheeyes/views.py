from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants





class Introduction(Page):
    form_model = models.Player
    form_fields = ['eye_practice']

class Introduction_Result(Page):

    def vars_for_template(self):
        return{
        'eye_practice' : self.player.eye_practice
        }

class Question1(Page):
    form_model = models.Player
    form_fields = ['eye_q1']


class Question2(Page):
    form_model = models.Player
    form_fields = ['eye_q2']


class Question3(Page):
    form_model = models.Player
    form_fields = ['eye_q3']


class Question4(Page):
    form_model = models.Player
    form_fields = ['eye_q4']


class Question5(Page):
    form_model = models.Player
    form_fields = ['eye_q5']


class Question6(Page):
    form_model = models.Player
    form_fields = ['eye_q6']


class Question7(Page):
    form_model = models.Player
    form_fields = ['eye_q7']


class Question8(Page):
    form_model = models.Player
    form_fields = ['eye_q8']


class Question9(Page):
    form_model = models.Player
    form_fields = ['eye_q9']


class Question10(Page):
    form_model = models.Player
    form_fields = ['eye_q10']



class Question11(Page):
    form_model = models.Player
    form_fields = ['eye_q11']


class Question12(Page):
    form_model = models.Player
    form_fields = ['eye_q12']


class Question13(Page):
    form_model = models.Player
    form_fields = ['eye_q13']


class Question14(Page):
    form_model = models.Player
    form_fields = ['eye_q14']


class Question15(Page):
    form_model = models.Player
    form_fields = ['eye_q15']


class Question16(Page):
    form_model = models.Player
    form_fields = ['eye_q16']


class Question17(Page):
    form_model = models.Player
    form_fields = ['eye_q17']


class Question18(Page):
    form_model = models.Player
    form_fields = ['eye_q18']


class Question19(Page):
    form_model = models.Player
    form_fields = ['eye_q19']


class Question20(Page):
    form_model = models.Player
    form_fields = ['eye_q20']


class Question21(Page):
    form_model = models.Player
    form_fields = ['eye_q21']


class Question22(Page):
    form_model = models.Player
    form_fields = ['eye_q22']


class Question23(Page):
    form_model = models.Player
    form_fields = ['eye_q23']


class Question24(Page):
    form_model = models.Player
    form_fields = ['eye_q24']


class Question25(Page):
    form_model = models.Player
    form_fields = ['eye_q25']


class Question26(Page):
    form_model = models.Player
    form_fields = ['eye_q26']


class Question27(Page):
    form_model = models.Player
    form_fields = ['eye_q27']


class Question28(Page):
    form_model = models.Player
    form_fields = ['eye_q28']






page_sequence = [
    Introduction,
    Introduction_Result,
    Question1,
    Question2,
    Question3,
    Question4,
    Question5,
    Question6,
    Question7,
    Question8,
    Question9,
    Question10,
    Question11,
    Question12,
    Question13,
    Question14,
    Question15,
    Question16,
    Question17,
    Question18,
    Question19,
    Question20,
    Question21,
    Question22,
    Question23,
    Question24,
    Question25,
    Question26,
    Question27,
    Question28


]
