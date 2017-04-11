from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants

def vars_for_all_templates(self):



    return {
        'correct0': self.player.correct0,
        'correct1': self.player.correct1,
        'correct2': self.player.correct2,
        'correct3': self.player.correct3,
        'correct4': self.player.correct4,
        'correct5': self.player.correct5,
        'correct6': self.player.correct6,
        'correct7': self.player.correct7,
        'correct8': self.player.correct8,
        'correct9': self.player.correct9,
        'correct10': self.player.correct10,
        'correct11': self.player.correct11,
        'correct12': self.player.correct12,
        'correct13': self.player.correct13,
        'correct14': self.player.correct14,
        'correct15': self.player.correct15,
        'correct16': self.player.correct16,
        'correct17': self.player.correct17,
        'correct18': self.player.correct18,
        'correct19': self.player.correct19,
        'correct20': self.player.correct20,
        'correct21': self.player.correct21,
        'correct22': self.player.correct22,
        'correct23': self.player.correct23,
        'correct24': self.player.correct24,
        'correct25': self.player.correct25,
        'correct26': self.player.correct26,
        'correct27': self.player.correct27,
        'correct28': self.player.correct28,
        'correct_Total' : self.player.correct1 + self.player.correct2 + self.player.correct3 + self.player.correct4 + self.player.correct5 + self.player.correct6 + self.player.correct7 + self.player.correct8 + self.player.correct9 + self.player.correct10 + self.player.correct11 + self.player.correct12 + self.player.correct13 + self.player.correct14 + self.player.correct15 + self.player.correct16 + self.player.correct17 + self.player.correct18 + self.player.correct19 + self.player.correct20 + self.player.correct21 + self.player.correct22 + self.player.correct23 + self.player.correct24 + self.player.correct25 + self.player.correct26 + self.player.correct27 + self.player.correct28,
        'Pseudo_Round' : self.player.Pseudo_Round
    }


class Start(Page):
    pass


class Introduction(Page):
    form_model = models.Player
    form_fields = ['eye_practice']


class Introduction_Result(Page):

    def vars_for_template(self):
        if self.player.eye_practice == 2:
            self.player.correct0=1
        else:
            self.player.correct0=0
        return{
        'eye_practice' : self.player.eye_practice,
        'correct0' : self.player.correct0
        }
    def before_next_page(self):
        self.player.Pseudo_Round+=3

class Question1(Page):
    form_model = models.Player
    form_fields = ['eye_q1']

    def before_next_page(self):
        self.player.Pseudo_Round+=4

class Question2(Page):

    def vars_for_template(self):
        if self.player.eye_q1 == 3:
            self.player.correct1=1
        else:
            self.player.correct1=0



    form_model = models.Player
    form_fields = ['eye_q2']

    def before_next_page(self):
        self.player.Pseudo_Round+=3

class Question3(Page):

    def vars_for_template(self):
        if self.player.eye_q2 == 4:
            self.player.correct2=1
        else:
            self.player.correct2=0

    form_model = models.Player
    form_fields = ['eye_q3']

    def before_next_page(self):
        self.player.Pseudo_Round+=4

class Question4(Page):
    def vars_for_template(self):
        if self.player.eye_q3 ==1:
            self.player.correct3=1
        else:
            self.player.correct3=0


    form_model = models.Player
    form_fields = ['eye_q4']

    def before_next_page(self):
        self.player.Pseudo_Round+=3

class Question5(Page):
    def vars_for_template(self):
        if self.player.eye_q4 == 2:
            self.player.correct4=1
        else:
            self.player.correct4=0



    form_model = models.Player
    form_fields = ['eye_q5']

    def before_next_page(self):
        self.player.Pseudo_Round+=4
class Question6(Page):

    def vars_for_template(self):
        if self.player.eye_q5 == 2:
            self.player.correct5=1
        else:
            self.player.correct5=0

    form_model = models.Player
    form_fields = ['eye_q6']

    def before_next_page(self):
        self.player.Pseudo_Round+=3
class Question7(Page):

    def vars_for_template(self):
        if self.player.eye_q6 == 3:
            self.player.correct6=1
        else:
            self.player.correct6=0

    form_model = models.Player
    form_fields = ['eye_q7']

    def before_next_page(self):
        self.player.Pseudo_Round+=4
class Question8(Page):

    def vars_for_template(self):
        if self.player.eye_q7 == 3:
            self.player.correct7=1
        else:
            self.player.correct7=0

    form_model = models.Player
    form_fields = ['eye_q8']

    def before_next_page(self):
        self.player.Pseudo_Round+=3

class Question9(Page):

    def vars_for_template(self):
        if self.player.eye_q8 == 1:
            self.player.correct8=1
        else:
            self.player.correct8=0

    form_model = models.Player
    form_fields = ['eye_q9']

    def before_next_page(self):
        self.player.Pseudo_Round+=4

class Question10(Page):
    def vars_for_template(self):
        if self.player.eye_q9 == 4:
            self.player.correct9=1
        else:
            self.player.correct9=0

    form_model = models.Player
    form_fields = ['eye_q10']

    def before_next_page(self):
        self.player.Pseudo_Round+=3.5

class Question11(Page):
    def vars_for_template(self):
        if self.player.eye_q10 == 3:
            self.player.correct10=1
        else:
            self.player.correct10=0


    form_model = models.Player
    form_fields = ['eye_q11']

    def before_next_page(self):
        self.player.Pseudo_Round+=4

class Question12(Page):
    def vars_for_template(self):
        if self.player.eye_q11 == 2:
            self.player.correct11=1
        else:
            self.player.correct11=0

    form_model = models.Player
    form_fields = ['eye_q12']

    def before_next_page(self):
        self.player.Pseudo_Round+=3

class Question13(Page):
    def vars_for_template(self):
        if self.player.eye_q12 == 4:
            self.player.correct12=1
        else:
            self.player.correct12=0


    form_model = models.Player
    form_fields = ['eye_q13']

    def before_next_page(self):
        self.player.Pseudo_Round+=4

class Question14(Page):
    def vars_for_template(self):
        if self.player.eye_q13 == 1:
            self.player.correct13=1
        else:
            self.player.correct13=0

    form_model = models.Player
    form_fields = ['eye_q14']

    def before_next_page(self):
        self.player.Pseudo_Round+=3


class Question15(Page):
    def vars_for_template(self):
        if self.player.eye_q14 == 2:
            self.player.correct14=1
        else:
            self.player.correct14=0


    form_model = models.Player
    form_fields = ['eye_q15']

    def before_next_page(self):
        self.player.Pseudo_Round+=4


class Question16(Page):
    def vars_for_template(self):
        if self.player.eye_q15 == 1:
            self.player.correct15=1
        else:
            self.player.correct15=0


    form_model = models.Player
    form_fields = ['eye_q16']

    def before_next_page(self):
        self.player.Pseudo_Round+=4

class Question17(Page):
    def vars_for_template(self):
        if self.player.eye_q16 == 1:
            self.player.correct16=1
        else:
            self.player.correct16=0


    form_model = models.Player
    form_fields = ['eye_q17']

    def before_next_page(self):
        self.player.Pseudo_Round+=3


class Question18(Page):
    def vars_for_template(self):
        if self.player.eye_q17 == 4:
            self.player.correct17=1
        else:
            self.player.correct17=0

    form_model = models.Player
    form_fields = ['eye_q18']

    def before_next_page(self):
        self.player.Pseudo_Round+=4


class Question19(Page):
    def vars_for_template(self):
        if self.player.eye_q18 == 1:
            self.player.correct18=1
        else:
            self.player.correct18=0

    form_model = models.Player
    form_fields = ['eye_q19']

    def before_next_page(self):
        self.player.Pseudo_Round+=3


class Question20(Page):
    def vars_for_template(self):
        if self.player.eye_q19 == 4:
            self.player.correct19=1
        else:
            self.player.correct19=0


    form_model = models.Player
    form_fields = ['eye_q20']

    def before_next_page(self):
        self.player.Pseudo_Round+=4


class Question21(Page):
    def vars_for_template(self):
        if self.player.eye_q20 == 3:
            self.player.correct20=1
        else:
            self.player.correct20=0


    form_model = models.Player
    form_fields = ['eye_q21']

    def before_next_page(self):
        self.player.Pseudo_Round+=3.5


class Question22(Page):
    def vars_for_template(self):
        if self.player.eye_q21 == 1:
            self.player.correct21=1
        else:
            self.player.correct21=0


    form_model = models.Player
    form_fields = ['eye_q22']

    def before_next_page(self):
        self.player.Pseudo_Round+=4


class Question23(Page):
    def vars_for_template(self):
        if self.player.eye_q22 == 4:
            self.player.correct22=1
        else:
            self.player.correct22=0


    form_model = models.Player
    form_fields = ['eye_q23']

    def before_next_page(self):
        self.player.Pseudo_Round+=3.5


class Question24(Page):
    def vars_for_template(self):
        if self.player.eye_q23 == 2:
            self.player.correct23=1
        else:
            self.player.correct23=0

    form_model = models.Player
    form_fields = ['eye_q24']

    def before_next_page(self):
        self.player.Pseudo_Round+=4


class Question25(Page):
    def vars_for_template(self):
        if self.player.eye_q24 == 1:
            self.player.correct24=1
        else:
            self.player.correct24=0

    form_model = models.Player
    form_fields = ['eye_q25']

    def before_next_page(self):
        self.player.Pseudo_Round+=3.5


class Question26(Page):
    def vars_for_template(self):
        if self.player.eye_q25 == 4:
            self.player.correct25=1
        else:
            self.player.correct25=0

    form_model = models.Player
    form_fields = ['eye_q26']

    def before_next_page(self):
        self.player.Pseudo_Round+=4


class Question27(Page):
    def vars_for_template(self):
        if self.player.eye_q26 == 3:
            self.player.correct26=1
        else:
            self.player.correct26=0


    form_model = models.Player
    form_fields = ['eye_q27']

    def before_next_page(self):
        self.player.Pseudo_Round+=4


class Question28(Page):
    def vars_for_template(self):
        if self.player.eye_q27 == 3:
            self.player.correct27=1
        else:
            self.player.correct27=0

    form_model = models.Player
    form_fields = ['eye_q28']



class RMET_Result(Page):
    def vars_for_template(self):
        if self.player.eye_q28 == 3:
            self.player.correct28=1
        else:
            self.player.correct28=0


        self.player.correct_total= self.player.correct1 + self.player.correct2 + self.player.correct3 + self.player.correct4 + self.player.correct5 + self.player.correct6 + self.player.correct7 + self.player.correct8 + self.player.correct9 + self.player.correct10 + self.player.correct11 + self.player.correct12 + self.player.correct13 + self.player.correct14 + self.player.correct15 + self.player.correct16 + self.player.correct17 + self.player.correct18 + self.player.correct19 + self.player.correct20 + self.player.correct21 + self.player.correct22 + self.player.correct23 + self.player.correct24 + self.player.correct25 + self.player.correct26 + self.player.correct27 + self.player.correct28

        return{
            'Total' : self.player.correct_total + 1,
        }




page_sequence = [
    Start,
    Introduction,
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
    Question28,
    RMET_Result,

]
