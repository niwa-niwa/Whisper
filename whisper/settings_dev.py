from .settings_common import *


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

#Logging Configure
LOGGING ={
    'version': 1, #1固定
    'disable.existing_loggers': False,

    #ロガー設定
    'loggers': {
        #Djangoが利用するロガー
        'django':{
            'handlers':['console'],
            'level':'INFO',
        },
        # whisperアプリケーションが利用するロガー
        'whisper':{
            'handlers':['console'],
            'level':'DEBUG',
        },
    },

    # ハンドラの設定
    'handlers':{
        'console':{
            'level':'DEBUG',
            'class':'logging.StreamHandler',
            'formatter':'dev'
        },
    },

    # フォーマッタの設定
    'formatters':{
        'dev':{
            'format':'\t'.join([
                '%(asctime)s',
                '[%(levelname)s]',
                '%(pathname)s(Line:5(lineno)d)',
                '%(message)s'
            ])
        },
    }
}

# 開発用の設定
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
