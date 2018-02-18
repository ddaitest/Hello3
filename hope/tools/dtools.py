import datetime
import time


def a1():
    # 字符串时间转时间搓
    datestr1 = '2015-06-06 10:10:10'
    print('datestr to time :', time.mktime(time.strptime(datestr1, "%Y-%m-%d %H:%M:%S")))

    # 时间搓转格式化时间字符串
    time1 = time.time()
    print
    'time to datestr :', time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time1))

    # datetime对象转时间搓
    datetime1 = datetime.datetime.now()
    print
    'datetime to time :', time.mktime(datetime1.timetuple())

    # 时间戳转datetime对象
    t1 = time.time()
    t2 = t1 + 20
    d1 = datetime.datetime.fromtimestamp(t1)
    d2 = datetime.datetime.fromtimestamp(t2)
    print
    'time1 to datetime1 :', datetime.datetime.fromtimestamp(t1)
    print
    'time2 to datetime2 :', datetime.datetime.fromtimestamp(t2)
    print
    'seconds diff :', (d2 - d1).seconds
    return 1
