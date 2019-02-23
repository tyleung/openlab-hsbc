#! /usr/bin/python3
# -*- coding: utf-8 -*-
import random
import time

class Rand_Gen(object):

    gender_lst = ['Male', 'Female']
    m_titles = ['Mr.']
    f_titles = ['Ms.'] 
    edus = ['Primary School', 'High school', 'Bachelor',
            'Master', 'Ph.D']

    @staticmethod
    def get_rand_gender(title='Mr.'):
        if title == 'Mr.':
            return 'Male'
        else:
            return 'Female'
        # return Rand_Gen.gender_lst[random.randint(0, 1)]

    @staticmethod
    def get_rand_title(gender='Male'):
        if gender.startswith('M'):
            title = Rand_Gen.m_titles[random.randint(0, len(Rand_Gen.m_titles) - 1)]
        else:
            title = Rand_Gen.f_titles[random.randint(0, len(Rand_Gen.f_titles) - 1)]
        return title
        

    @staticmethod
    def get_rand_date():
        a1=(1976,1,1,0,0,0,0,0,0)         #设置开始日期时间元组（1976-01-01 00：00：00）
        a2=(1990,12,31,23,59,59,0,0,0)    #设置结束日期时间元组（1990-12-31 23：59：59）

        start=time.mktime(a1)    #生成开始时间戳
        end=time.mktime(a2)      #生成结束时间戳

        #随机生成10个日期字符串
        # for i in range(10):      
        t=random.randint(start,end)    #在开始和结束时间戳中随机取出一个
        date_touple=time.localtime(t)          #将时间戳生成时间元组
        date=time.strftime("%Y%m%d",date_touple)  #将时间元组转成格式化字符串（1976-05-21）
        return date

    @staticmethod
    def get_rand_num(len=5):
        id = str(random.randint(1000000000, 9999999999)).ljust(10, '0')
        return id[-1 * len]

    @staticmethod
    def get_rand_id():
        id = str(random.randint(1000000000, 9999999999)).ljust(10, '0')
        return id
        
    @staticmethod
    def get_rand_edu():
        return Rand_Gen.edus[random.randint(0, len(Rand_Gen.edus) - 1)]