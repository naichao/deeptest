
from datetime import date, datetime,time

__author__ = u'奶茶哥'

if __name__ == '__main__':
    # 获取今天的日期
    today = date.today()
    print('今天日期是：%s' % today)

    # 把年月日分开年月日三部分获取，然后展示
    print('今天日期是：%s %s %s' % (today.day,today.month,today.year))

    # 获取星期几对于的序号
    weekday_num = today.weekday()
    print('今天weekday是：%s' % weekday_num)

    # 输出可读性更好的星期几
    weekdays = ('Monday','Tuesday','Wednesday',
                'Thursday','Firday','Saturday','Sunday')
    print('今天是：%s' % weekdays[weekday_num])

    print('_' * 30)

    # 时间
    today_now = datetime.now()
    print('现在时间是：%s' % today_now)

    # 用time造个时间
    t = time(hour=12,minute=20,second=30,microsecond=200)
    print('自己造的时间是：%s' % t )

    # 再造个日期出来
    d = datetime(year=2018,month=4,day=22,hour=17,minute=7,second=30)
    print('自己造的日期是：%s' % d)

    print('-' * 30)
    import time
    localtime = time.asctime(time.localtime())
    print('当前默认时间日期格式是：%s' % localtime)

    # 格式：年-月-日 时：分：秒 星期几
    print('24小时制格式：', time.strftime('%Y-%m-%d %H:%M:%S %A',
                                    time.localtime()))
    print('12小时制格式：',time.strftime('%Y-%m-%d %I:%M:%S %a',
                                   time.localtime()))

    # 带a.m或p.m
    print('带a.m/p.m时间格式：',time.strftime('%Y-%m-%d %H:%M:%S %p %A',
                                        time.localtime()))

    # 带时区的时间格式(时区乱码没有解决)
    print('带时区的时间格式：',time.strftime('%Y-%m-%d %H:%M:%S %p %A %z',
                                    time.localtime()))







