#! /usr/bin/python3
# -*- coding: utf-8 -*-
import random
import time

random.seed(time.time())

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
    def get_rand_date(start: tuple = (), end: tuple = ()) -> str:
        a1=(1976,1,1,0,0,0,0,0,0) if not start else start     #设置开始日期时间元组（1976-01-01 00：00：00）
        a2=(1990,12,31,23,59,59,0,0,0) if not end else end    #设置结束日期时间元组（1990-12-31 23：59：59）

        start=time.mktime(a1)    #生成开始时间戳
        end=time.mktime(a2)      #生成结束时间戳

        #随机生成10个日期字符串
        # for i in range(10):      
        t=random.randint(start,end)    #在开始和结束时间戳中随机取出一个
        date_tuple=time.localtime(t)          #将时间戳生成时间元组
        date=time.strftime("%Y%m%d",date_tuple)  #将时间元组转成格式化字符串（1976-05-21）
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

    @staticmethod
    def get_rand_geo(hot_points: list = []) -> tuple:
        # generate geo coordinates in HK    
        hot_points = [
            (22.319303, 114.169394), (22.321588, 114.169495), (22.313238, 114.170533),
            (22.315634, 114.264360), (22.307365, 114.259740), (22.383694, 114.270938),
            (22.337897, 114.265368), (22.304289, 114.161463), (22.447479, 114.025369),
            (22.281974, 114.158280), (22.278379, 114.182186), (22.288271, 114.193914), 
            (22.264631, 114.237206), (22.276088, 114.145540), (22.295140, 114.168850)
        ] if not hot_points else hot_points

        position = hot_points[random.randint(0, len(hot_points)-1)]
        x = round(position[0] + (random.random() - 1) / 1000, 6)
        y = round(position[1] + (random.random() - 1) / 1000, 6)

        return (x, y)

    @staticmethod
    def get_rand_time():
        date = Rand_Gen.get_rand_date((2009,1,1,0,0,0,0,0,0), (2018,12,31,23,59,59,0,0,0))
        r = random.random()
        m = random.randint(0, 59)
        if r < 0.6:
            time = f'{random.randint(10, 18)}:{m}:00'
        elif r < 0.9:
            time = f'{random.randint(20, 24)}:{m}:00'
        else:
            sparse_time = ['08', '09', '19', '01']
            time = f'{sparse_time[random.randint(0, 3)]}:{m}:00'
        return date+'T'+time+'Z'

    @staticmethod
    def get_rand_bank_id() -> str:

        bank_list = ['hsbc.01.hk.hsbc', 'hsbc.02.hk.hsbc', 'hsbc.02.uk.uk', 'hsbc.01.uk.uk']

        r  = random.random()
        if r < 0.4:
            return bank_list[0]
        elif r < 0.8:
            return bank_list[1]
        elif r < 0.9:
            return bank_list[2]
        else:
            return bank_list[3]

    @staticmethod
    def get_rand_trans_type() -> str:

        trans_types = ['purchase', 'transfer']

        r  = random.random()
        if r < 0.7:
            return trans_types[0]
        else:
            return trans_types[1]

    @staticmethod
    def get_rand_prod_type() -> str:
        product_types = {
            'hot_types': ['Electronics', 'Fashion', 'PersonalCare', 'Movie&Music'],
            'mid_types': ['Softwares', 'Baby', 'Books', 'Household'],
            'cold_types': ['Automotive', 'Pet', 'Industrial']
        }
        
        r = random.random()
        if r < 0.6:
            upper_bound = len(product_types['hot_types']) - 1
            return product_types['hot_types'][random.randint(0, upper_bound)]
        elif r < 0.9:
            upper_bound = len(product_types['mid_types']) - 1
            return product_types['mid_types'][random.randint(0, upper_bound)]
        else:
            upper_bound = len(product_types['cold_types']) - 1
            return product_types['cold_types'][random.randint(0, upper_bound)]

    @staticmethod
    def get_rand_curr_type() -> str:
        currency_types = ['USD', 'HKD', 'CNY', 'EUR']

        r  = random.random()
        if r < 0.1:
            return currency_types[0]
        elif r < 0.6:
            return currency_types[1]
        elif r < 0.9:
            return currency_types[2]
        else:
            return currency_types[3]

    @staticmethod
    def get_rand_amount(is_balance: bool = False):
        # get random transaction amount or balance
        base = random.randint(1, 9)

        r = random.random()
        if is_balance:
            return str(base*1000) if r > 0.7 else str(base*10000)

        r = random.random()
        if r < 0.5:
            return str(-base)
        elif r < 0.7:
            return str((base-10)*100)
        else:
            return str((base-10)*1000)

        
if __name__ == '__main__':
    for i in range(10):
        print(Rand_Gen.get_rand_geo()) 