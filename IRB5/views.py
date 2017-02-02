from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants

def vars_for_all_templates(self):
    return {
        'v': self.player.participant.vars['v']
    }

class IRB(Page):
    form_model = models.Player
    form_fields = ['IRB']



page_sequence = [
    IRB
]
