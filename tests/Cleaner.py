## @Ver     0.8v
## @Author  Phillip Park
## @Date    2017/12/12
## @Details 파일들을 정리하고 간단한 처리

import os, glob

from ..buzzz.settings import INSTALLED_APPS


class Cleaner:
    def __init__(self):
        self.apps = [app for app in INSTALLED_APPS if 'django' not in app and 'rest_framework' not in app]
        print(self.apps)

    def clean_migrations(self):
        pass
