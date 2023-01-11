from django.apps import AppConfig
from django.conf import settings


'''
class TempConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'temp'

    # 앱이 실행될때 operator.start() 실행
    def ready(self):
        if settings.SCHEDULER_DEFAULT:
            from . import operator
            operator.start()
'''
