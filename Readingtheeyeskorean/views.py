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






page_sequence = [
    Introduction,
    Introduction_Result,
    Question1,


]
