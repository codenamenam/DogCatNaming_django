from .Search.searchHandler import search
from apscheduler.schedulers.background import BackgroundScheduler

# 1주일마다 주기적으로 search 실행
# pythonanywhere에서는 schedule 대신 task로 작업 실행 권장

def start():
    '''
    sched = BackgroundScheduler(timezone='Asia/Seoul')
    sched.add_job(search, 'interval', days=7, id='test')
    sched.start()
    '''