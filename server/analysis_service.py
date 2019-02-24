#! /usr/bin/python3
# -*- coding: utf-8 -*-
import os
import sys
import json
import random
import time
import logging

from datetime import datetime as dt
from os.path import join as pjoin

from utils.rand_gen import Rand_Gen

random.seed(5001)
logging.basicConfig(level=logging.INFO,
                    format='[%(asctime)s][%(name)s][%(levelname)s][%(message)s]')
logger = logging.getLogger(__name__)


class Analyst(object):

    def __init__(self, user_db, trans_db):
        self.user_db = user_db
        self.trans_db = trans_db
        self.result = {'age': [], 'title': []}
        # self.data_user = self.load_user()
        # self.data_trans = self.load_trans()

    def load_user(self, modify=False, rewrite=False):
        with open(self.user_db, 'r') as f:
            customers = json.load(f)
        if modify:
            # randomly generate customer ID.
            for customer in customers:
                # customer['customer_id'] = Rand_Gen.get_rand_id()
                # customer['date_of_birth'] = Rand_Gen.get_rand_date()
                customer['age'] = (dt.now() - dt.strptime(str(customer['date_of_birth']), '%Y%m%d')).days // 365
                # customer['dependants'] = Rand_Gen.get_rand_num(len=1)
                customer['gender'] = Rand_Gen.get_rand_gender(
                    title=customer['title'])
                # customer['title'] = Rand_Gen.get_rand_title(gender=customer['gender'])
                # customer['highest_education_attained'] = Rand_Gen.get_rand_edu()

        if rewrite:
            json_str = json.dumps(customers)
        with open(self.user_db, 'w') as f:
            f.write(json_str)

        logger.info(
            f"Load user data successful. user data length: {len(customers)}")
        return customers

    def load_trans(self):
        with open(self.trans_db, 'r') as f:
            trans = json.load(f)
        trans = trans['transactions']
        logger.info(
            f"Load transactions data successful. trans data length: {len(trans)}")
        return trans

    def analysis_users(self, userlist: list):

        cus_dict = {}
        with open(self.user_db, 'r') as f:
            customers = json.load(f)
            for c in customers:
                cus_dict[c['customer_id']] = c

        age_bins = [0, 10, 15, 21, 30, 35, 100]
        credit_bins = [10000, 20000, 30000, 40000, 50000]
        info = {
            'age': dict.fromkeys(age_bins, 0),
            'credit': dict.fromkeys(credit_bins, 0),
            'edu': {},
            'gender': {}
        }
        for user in userlist:
            customer = cus_dict[user]

            age = int(customer['age'])
            if age < age_bins[0]:
                info['age'][age_bins[0]] += 1
            elif age < age_bins[1]:
                info['age'][age_bins[1]] += 1
            elif age < age_bins[2]:
                info['age'][age_bins[2]] += 1
            elif age < age_bins[3]:
                info['age'][age_bins[3]] += 1
            elif age < age_bins[4]:
                info['age'][age_bins[4]] += 1
            elif age < age_bins[5]:
                info['age'][age_bins[5]] += 1
            elif age < age_bins[6]:
                info['age'][age_bins[6]] += 1

            amount = float(''.join(customer['credit_limit']['amount'][1:].split(',')))
            if amount < credit_bins[0]:
                info['credit'][credit_bins[0]] += 1
            elif amount < credit_bins[1]:
                info['credit'][credit_bins[1]] += 1
            elif amount < credit_bins[2]:
                info['credit'][credit_bins[2]] += 1
            elif amount < credit_bins[3]:
                info['credit'][credit_bins[3]] += 1
            elif amount < credit_bins[4]:
                info['credit'][credit_bins[4]] += 1
            else:
                info['credit'][100000] += 1

            if customer['highest_education_attained'] in info['edu']:
                info['edu'][customer['highest_education_attained']] += 1
            else:
                info['edu'][customer['highest_education_attained']] = 0

            if customer['gender'] in info['gender']:
                info['gender'][customer['gender']] += 1
            else:
                info['gender'][customer['gender']] = 0
        
        return info
        

# if __name__ == "__main__":
#     ana = Analyst(user_db='./server/data/customer_info.json', trans_db="./data/test.json")
#     li = ['5c710e1723d8c12d2754a9a5', '5c710e174e07fefa14c42cde', '5c710e17b302c9be32cf4860', '5c710e1776d1a539396b13e3', '5c710e17c234e14b08bedc88', '5c710e170a524e7efc793843', '5c710e1805351b8b177b0f7c', '5c710e172054460f7289a531', '5c710e17f2b50ee11cfc263c', '5c710e178321180c5d03263c', '5c710e17b69b90993590ae60', '5c710e17eae8fa7b12a3194e', '5c710e177c82a8e540c0e107', '5c710e176f0ae8f1387b051f']
#     result = ana.analysis_users(li)
#     print('sth')
