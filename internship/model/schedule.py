#coding=utf-8
from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.schedulers.background import BackgroundScheduler
from .sign import *


schedudler = BackgroundScheduler()
# 定义一个job类，完成想要做的事
def start_job():
    signmain()

# 定时每天执行任务
schedudler.add_job(start_job,'cron',day_of_week='0-6',hour=1,minute=0,second=0)
schedudler.add_job(start_job,'cron',day_of_week='0-6',hour=2,minute=0,second=0)
schedudler.add_job(start_job,'cron',day_of_week='0-6',hour=3,minute=0,second=0)
schedudler.add_job(start_job,'cron',day_of_week='0-6',hour=4,minute=0,second=0)
schedudler.add_job(start_job,'cron',day_of_week='0-6',hour=5,minute=0,second=0)
schedudler.add_job(start_job,'cron',day_of_week='0-6',hour=6,minute=0,second=0)
schedudler.add_job(start_job,'cron',day_of_week='0-6',hour=7,minute=0,second=0)
schedudler.add_job(start_job,'cron',day_of_week='0-6',hour=8,minute=0,second=0)
schedudler.add_job(start_job,'cron',day_of_week='0-6',hour=9,minute=0,second=0)
schedudler.add_job(start_job,'cron',day_of_week='0-6',hour=10,minute=0,second=0)
schedudler.add_job(start_job,'cron',day_of_week='0-6',hour=11,minute=0,second=0)
schedudler.add_job(start_job,'cron',day_of_week='0-6',hour=12,minute=0,second=0)
schedudler.add_job(start_job,'cron',day_of_week='0-6',hour=13,minute=0,second=0)
schedudler.add_job(start_job,'cron',day_of_week='0-6',hour=14,minute=0,second=0)
schedudler.add_job(start_job,'cron',day_of_week='0-6',hour=15,minute=0,second=0)
schedudler.add_job(start_job,'cron',day_of_week='0-6',hour=16,minute=0,second=0)
schedudler.add_job(start_job,'cron',day_of_week='0-6',hour=17,minute=0,second=0)
schedudler.add_job(start_job,'cron',day_of_week='0-6',hour=18,minute=0,second=0)
schedudler.add_job(start_job,'cron',day_of_week='0-6',hour=19,minute=0,second=0)
schedudler.add_job(start_job,'cron',day_of_week='0-6',hour=20,minute=0,second=0)
schedudler.add_job(start_job,'cron',day_of_week='0-6',hour=21,minute=0,second=0)
schedudler.add_job(start_job,'cron',day_of_week='0-6',hour=22,minute=0,second=0)
schedudler.add_job(start_job,'cron',day_of_week='0-6',hour=23,minute=0,second=0)
schedudler.add_job(start_job,'cron',day_of_week='0-6',hour=0,minute=0,second=0)
schedudler.start()
