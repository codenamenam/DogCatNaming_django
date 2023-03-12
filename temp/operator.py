from .Search.searchHandler import search
from apscheduler.schedulers.background import BackgroundScheduler

# 서버 시작 시 search 예약실행, 1주일마다 정기적으로 실행

def start():
    sched = BackgroundScheduler(timezone='Asia/Seoul')
    sched.add_job(search, 'cron', hour=22, minute=30, id='test')
    sched.start()