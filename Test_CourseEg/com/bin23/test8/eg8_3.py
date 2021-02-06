import datetime

class DateTimer:
    __year = 0
    __month = 0
    __day = 0
    __hours = 0
    __minutes = 0
    __seconds = 0

    def __init__(self, y, m, d, hours, minutes, seconds):
        self.__year = y
        self.__month = m
        self.__day = d
        self.__hours = hours
        self.__minutes = minutes
        self.__seconds = seconds

    def getYear(self):
        return self.__year

    def setYear(self, year):
        self.__year = year

    def getMonth(self):
        return self.__month

    def setMonth(self, month):
        self.__month = month

    def getDay(self):
        return self.__day

    def setDay(self, day):
        self.__day = day

    def getHours(self):
        return self.__hours

    def setHours(self, hours):
        self.__hours = hours

    def getMinutes(self):
        return self.__minutes

    def setMinutes(self, minutes):
        self.__minutes = minutes

    def getSeconds(self):
        return self.__seconds

    def setSeconds(self, seconds):
        self.__seconds = seconds

    def getTime(self):
        print(dt.getYear(), "年", dt.getMonth(), "月", dt.getDay(), "日", dt.getHours(), "时", dt.getMinutes(), "分", dt.getSeconds(), "秒")


if __name__ == '__main__':
    now = datetime.datetime.now()
    # print(now)
    # print(now.year)
    # print(now.month)
    # print(now.day)
    # print(now.hour)
    # print(now.minute)
    # print(now.second)
    # print(now.microsecond)

    dt = DateTimer(now.year, now.month, now.day, now.hour, now.minute, now.second)
    dt.getTime()
