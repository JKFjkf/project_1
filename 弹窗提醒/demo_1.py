import win32api, win32con, time

from apscheduler.schedulers.blocking import BlockingScheduler


def DrunkWater():
    win32api.MessageBox(0, "别jb摸鱼了！", "摸鱼", win32con.MB_OK)


# BlockingScheduler

scheduler = BlockingScheduler()

scheduler.add_job(DrunkWater, 'interval', minutes=1)

if __name__ == '__main__':

    while True:
        scheduler.start()

        time.sleep(1)