from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants


class Question1(Page):
    form_model=models.Player
    form_fields=['Rubin_q1']

class Question2(Page):
    form_model=models.Player
    form_fields=['Rubin_q2']

class Question3(Page):
    form_model=models.Player
    form_fields=['Rubin_q3']

class Question4(Page):
    form_model=models.Player
    form_fields=['Rubin_q4']

class Question5(Page):
    form_model=models.Player
    form_fields=['Rubin_q5']



page_sequence = [
    Question1,
    Question2,
    Question3,
    Question4,
    Question5,
]
