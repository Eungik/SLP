import os
from os import environ

import dj_database_url
from boto.mturk import qualification

import otree.settings


BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# the environment variable OTREE_PRODUCTION controls whether Django runs in
# DEBUG mode. If OTREE_PRODUCTION==1, then DEBUG=False
if environ.get('OTREE_PRODUCTION') not in {None, '', '0'}:
    DEBUG = False
else:
    DEBUG = True

ADMIN_USERNAME = 'admin'

# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

# don't share this with anybody.
SECRET_KEY = 's$hjy_t78+6nm+#hpg2789w-#e^nw*ms&900m3he4%i5=9j#%&'

# To use a database other than sqlite,
# set the DATABASE_URL environment variable.
# Examples:
# postgres://USER:PASSWORD@HOST:PORT/NAME
# mysql://USER:PASSWORD@HOST:PORT/NAME

DATABASES = {
    'default': dj_database_url.config(
        default='sqlite:///' + os.path.join(BASE_DIR, 'db.sqlite3')
    )
}

# AUTH_LEVEL:
# If you are launching a study and want visitors to only be able to
# play your app if you provided them with a start link, set the
# environment variable OTREE_AUTH_LEVEL to STUDY.
# If you would like to put your site online in public demo mode where
# anybody can play a demo version of your game, set OTREE_AUTH_LEVEL
# to DEMO. This will allow people to play in demo mode, but not access
# the full admin interface.

AUTH_LEVEL = environ.get('OTREE_AUTH_LEVEL')

# setting for integration with AWS Mturk
AWS_ACCESS_KEY_ID = environ.get('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = environ.get('AWS_SECRET_ACCESS_KEY')


# e.g. EUR, CAD, GBP, CHF, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'USD'
USE_POINTS = False


# e.g. en, de, fr, it, ja, zh-hans
# see: https://docs.djangoproject.com/en/1.9/topics/i18n/#term-language-code
LANGUAGE_CODE = 'en'

# if an app is included in SESSION_CONFIGS, you don't need to list it here
# if an app is included in SESSION_CONFIGS, you don't need to list it here
INSTALLED_APPS = ['otree']

# SENTRY_DSN = ''

DEMO_PAGE_INTRO_TEXT = """
oTree games
"""

# from here on are qualifications requirements for workers
# see description for requirements on Amazon Mechanical Turk website:
# http://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI/ApiReference_QualificationRequirementDataStructureArticle.html
# and also in docs for boto:
# https://boto.readthedocs.org/en/latest/ref/mturk.html?highlight=mturk#module-boto.mturk.qualification

mturk_hit_settings = {
    'keywords': ['easy', 'bonus', 'choice', 'study'],
    'title': 'Title for your experiment',
    'description': 'Description for your experiment',
    'frame_height': 500,
    'preview_template': 'global/MTurkPreview.html',
    'minutes_allotted_per_assignment': 60,
    'expiration_hours': 7*24,  # 7 days
    # 'grant_qualification_id': 'YOUR_QUALIFICATION_ID_HERE',# to prevent retakes
    'qualification_requirements': [
        # qualification.LocaleRequirement("EqualTo", "US"),
        # qualification.PercentAssignmentsApprovedRequirement("GreaterThanOrEqualTo", 50),
        # qualification.NumberHitsApprovedRequirement("GreaterThanOrEqualTo", 5),
        # qualification.Requirement('YOUR_QUALIFICATION_ID_HERE', 'DoesNotExist')
    ]
}

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = {
    'real_world_currency_per_point': 0.01,
    'participation_fee': 10.00,
    'num_bots': 6,
    'doc': "",
    'mturk_hit_settings': mturk_hit_settings,
}



SESSION_CONFIGS = [
    {
        'name': 'SLP_2017_Chn',
        'display_name': 'SLP2017_Chinese',
        'num_demo_participants': 3,
        'app_sequence': ['SLPintro_Chn','Rubinstein_Chn','Race_intro_Chn','Race5_3_Chn','Race10_3_Chn','Race15_3_Chn','Race19_3_Chn','Readingtheeyes_Chn','Result_Race_Chn' ],
    },
    {
        'name': 'SLP2017_v1',
        'display_name': 'SLP2017_v1',
        'num_demo_participants': 3,
        'app_sequence': ['SLPintro','Rubinstein','Race_intro','Race5_3' ,'Race10_3','Race', 'Race19_3','Readingtheeyes','Result_Race'],
        'winning_number': 5
    },
    {
        'name': 'SLP2017_v2',
        'display_name': 'SLP2017_v2',
        'num_demo_participants': 3,
        'app_sequence': ['SLPintro', 'Rubinstein', 'Race_intro', 'Race5_3', 'Race10_3',  'Race19_3', 'Race',
                         'Readingtheeyes', 'Result_Race'],
    },
    {
        'name': 'SLP2017_v3',
        'display_name': 'SLP2017_v3',
        'num_demo_participants': 3,
        'app_sequence': ['SLPintro', 'Rubinstein', 'Race_intro', 'Race5_3', 'Race', 'Race10_3', 'Race19_3',
                         'Readingtheeyes', 'Result_Race'],
    },
    {
        'name': 'SLP2017_v4',
        'display_name': 'SLP2017_v4',
        'num_demo_participants': 3,
        'app_sequence': ['SLPintro', 'Rubinstein', 'Race_intro', 'Race5_3', 'Race', 'Race19_3', 'Race10_3',
                         'Readingtheeyes', 'Result_Race'],
    },
    {
        'name': 'SLP2017_v5',
        'display_name': 'SLP2017_v5',
        'num_demo_participants': 3,
        'app_sequence': ['SLPintro', 'Rubinstein', 'Race_intro', 'Race5_3', 'Race19_3', 'Race10_3', 'Race',
                         'Readingtheeyes', 'Result_Race'],
    },
    {
        'name': 'SLP2017_v6',
        'display_name': 'SLP2017_v6',
        'num_demo_participants': 3,
        'app_sequence': ['SLPintro', 'Rubinstein', 'Race_intro', 'Race5_3', 'Race19_3', 'Race', 'Race10_3',
                         'Readingtheeyes', 'Result_Race'],
    },
    {
        'name': 'SLP2017_v7',
        'display_name': 'SLP2017_v7',
        'num_demo_participants': 3,
        'app_sequence': ['SLPintro', 'Rubinstein', 'Race_intro', 'Race10_3', 'Race5_3', 'Race', 'Race19_3',
                         'Readingtheeyes', 'Result_Race'],
    },
    {
        'name': 'SLP2017_v8',
        'display_name': 'SLP2017_v8',
        'num_demo_participants': 3,
        'app_sequence': ['SLPintro', 'Rubinstein', 'Race_intro', 'Race10_3', 'Race5_3', 'Race19_3', 'Race',
                         'Readingtheeyes', 'Result_Race'],
    },
    {
        'name': 'SLP2017_v9',
        'display_name': 'SLP2017_v9',
        'num_demo_participants': 3,
        'app_sequence': ['SLPintro', 'Rubinstein', 'Race_intro', 'Race10_3', 'Race', 'Race5_3', 'Race19_3',
                         'Readingtheeyes', 'Result_Race'],
    },
    {
        'name': 'SLP2017_v10',
        'display_name': 'SLP2017_v10',
        'num_demo_participants': 3,
        'app_sequence': ['SLPintro', 'Rubinstein', 'Race_intro', 'Race10_3', 'Race', 'Race19_3', 'Race5_3',
                         'Readingtheeyes', 'Result_Race'],
    },
    {
        'name': 'SLP2017_v11',
        'display_name': 'SLP2017_v11',
        'num_demo_participants': 3,
        'app_sequence': ['SLPintro', 'Rubinstein', 'Race_intro', 'Race10_3',  'Race19_3', 'Race5_3', 'Race',
                         'Readingtheeyes', 'Result_Race'],
    },
    {
        'name': 'SLP2017_v12',
        'display_name': 'SLP2017_v12',
        'num_demo_participants': 3,
        'app_sequence': ['SLPintro', 'Rubinstein', 'Race_intro', 'Race10_3', 'Race19_3', 'Race', 'Race5_3',
                         'Readingtheeyes', 'Result_Race'],
    },
    {
        'name': 'SLP2017_v13',
        'display_name': 'SLP2017_v13',
        'num_demo_participants': 3,
        'app_sequence': ['SLPintro', 'Rubinstein', 'Race_intro', 'Race', 'Race5_3', 'Race10_3', 'Race19_3',
                         'Readingtheeyes', 'Result_Race'],
    },
    {
        'name': 'SLP2017_v14',
        'display_name': 'SLP2017_v14',
        'num_demo_participants': 3,
        'app_sequence': ['SLPintro', 'Rubinstein', 'Race_intro', 'Race', 'Race5_3', 'Race19_3',  'Race10_3',
                         'Readingtheeyes', 'Result_Race'],
    },
    {
        'name': 'SLP2017_v15',
        'display_name': 'SLP2017_v15',
        'num_demo_participants': 3,
        'app_sequence': ['SLPintro', 'Rubinstein', 'Race_intro', 'Race', 'Race10_3', 'Race5_3', 'Race19_3',
                         'Readingtheeyes', 'Result_Race'],
    },
    {
        'name': 'SLP2017_v16',
        'display_name': 'SLP2017_v16',
        'num_demo_participants': 3,
        'app_sequence': ['SLPintro', 'Rubinstein', 'Race_intro', 'Race', 'Race10_3', 'Race19_3', 'Race5_3',
                         'Readingtheeyes', 'Result_Race'],
    },
    {
        'name': 'SLP2017_v17',
        'display_name': 'SLP2017_v17',
        'num_demo_participants': 3,
        'app_sequence': ['SLPintro', 'Rubinstein', 'Race_intro', 'Race', 'Race19_3', 'Race5_3', 'Race10_3',
                         'Readingtheeyes', 'Result_Race'],
    },
    {
        'name': 'SLP2017_v18',
        'display_name': 'SLP2017_v18',
        'num_demo_participants': 3,
        'app_sequence': ['SLPintro', 'Rubinstein', 'Race_intro', 'Race', 'Race19_3', 'Race10_3', 'Race5_3',
                         'Readingtheeyes', 'Result_Race'],
    },
    {
        'name': 'SLP2017_v19',
        'display_name': 'SLP2017_v19',
        'num_demo_participants': 3,
        'app_sequence': ['SLPintro', 'Rubinstein', 'Race_intro', 'Race19_3', 'Race5_3', 'Race10_3', 'Race',
                         'Readingtheeyes', 'Result_Race'],
    },
    {
        'name': 'SLP2017_v20',
        'display_name': 'SLP2017_v20',
        'num_demo_participants': 3,
        'app_sequence': ['SLPintro', 'Rubinstein', 'Race_intro', 'Race19_3', 'Race5_3',  'Race', 'Race10_3',
                         'Readingtheeyes', 'Result_Race'],
    },
    {
        'name': 'SLP2017_v21',
        'display_name': 'SLP2017_v21',
        'num_demo_participants': 3,
        'app_sequence': ['SLPintro', 'Rubinstein', 'Race_intro', 'Race19_3', 'Race10_3', 'Race5_3', 'Race',
                         'Readingtheeyes', 'Result_Race'],
    },
    {
        'name': 'SLP2017_v22',
        'display_name': 'SLP2017_v22',
        'num_demo_participants': 3,
        'app_sequence': ['SLPintro', 'Rubinstein', 'Race_intro', 'Race19_3', 'Race10_3', 'Race', 'Race5_3',
                         'Readingtheeyes', 'Result_Race'],
    },
    {
        'name': 'SLP2017_v23',
        'display_name': 'SLP2017_v23',
        'num_demo_participants': 3,
        'app_sequence': ['SLPintro', 'Rubinstein', 'Race_intro', 'Race19_3', 'Race', 'Race5_3', 'Race10_3',
                         'Readingtheeyes', 'Result_Race'],
    },
    {
        'name': 'SLP2017_v24',
        'display_name': 'SLP2017_v24',
        'num_demo_participants': 3,
        'app_sequence': ['SLPintro', 'Rubinstein', 'Race_intro', 'Race19_3', 'Race', 'Race10_3', 'Race5_3',
                         'Readingtheeyes', 'Result_Race'],
    },

]

ROOMS = [
    {
        'name': 'SLP2017',
        'display_name': 'SLP2017',
        'participant_label_file': 'SLP.txt',
    },
]

# anything you put after the below line will override
# oTree's default settings. Use with caution.
otree.settings.augment_settings(globals())
