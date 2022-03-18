import threading
from config.config import work_num
from run_monitor import run_mon

if __name__ == '__main__':
    for item in range(work_num):
        work = threading.Thread(target=run_mon, args=(1,))
        work.start()
        print("第%s个线程启动成功。" % item)
