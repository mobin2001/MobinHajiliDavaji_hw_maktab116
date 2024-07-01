from persiantools.jdatetime import JalaliDate
from hijri_converter import Hijri,Gregorian
import datetime


class Date:
    date = datetime.date.today()
    def __init__(self):
        pass

    @classmethod
    def from_string(cls,date):
        date = list(map(int,date.split('-')))
        cls.date = datetime.date(date[-1],date[1],date[0])
        # return cls.date
    @staticmethod
    def is_valid_date(date):
        date = list(map(int,date.split('-')))
        try:
            datetime.date(date[-1],date[1],date[0])
            print ('valid date')
        except ValueError:
            print('invalid date')

    def to_shamsi():
        return JalaliDate.to_jalali(Date.date)

    def to_ghamari():
        today = list(map(int,str(Date.date).split('-')))
        return Gregorian(today[0],today[1],today[2]).to_hijri()

Date.from_string('11-09-2014')
Date.is_valid_date('13-112-2014')
print(Date.to_shamsi())
print(Date.to_ghamari())

