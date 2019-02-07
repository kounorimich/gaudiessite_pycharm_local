import environ

from .base import *

# Read .env if exists
env = environ.Env()
env.read_env(os.path.join(BASE_DIR, '.env.sample'))

############################
# Security###
#################

#####ALLOWED_HOSTS = env.list('ALLOWED_HOSTS')

ALLOWED_HOSTS = ['178.128.30.115', 'gaudies.jp']

SECRET_KEY = env('SECRET_KEY')

DEBUG = False

LOGGING = {
    #  バージョンは「1」固定
    'version': 1,
    # 既存のログ設定を無効化しない
    'disable_existing_loggers': False,
    # ログフォーマット
    'formatters': {
        'production': {
            'format': '%(asctime)s [%(levelname)s] %(process)d %(thread)d'
            '%(pathname)s:%(lineno)d %(message)s'
        }
    },
    # ハンドラ
    'handlers': {
        # ファイル出力用ハンドラ
        'file': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': '/var/log/{}.log'.format(PROJECT_NAME),
            'formatter': 'production',
        }
    },
    # ロガー
    'loggers': {
        #自作アプリケーション全般のログを拾うロガー
        '': {
            'handlers': ['file'],
            'level': 'INFO',
            'propagate': False,
        },

    },

}

DATABASES = {  # 本番環境ではMySQLを使うので、DB設定を上書き
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'gaudiessite',
        'USER': 'norimichi',
        'PASSWORD': '5hoo++heSinger',
        'HOST': 'localhost',
        'PORT': '3306',
        'ATOMIC_REQUESTS': True,
        'OPTIONS': {
            'charset': 'utf8mb4',
            'sql_mode': 'TRADITIONAL,NO_AUTO_VALUE_ON_ZERO',
        }
    }
}
