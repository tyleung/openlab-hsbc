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
    self.data_user = self.load_user()
    self.data_trans = self.load_trans()

  def load_user(self, modify=False, rewrite=False):
    with open(self.user_db, 'r') as f:
      customers = json.loads(f.read())
      if modify:
        # randomly generate customer ID.
        for customer in customers:
          # customer['customer_id'] = Rand_Gen.get_rand_id()
          # customer['date_of_birth'] = Rand_Gen.get_rand_date()
          customer['age'] = (dt.now() - dt.strptime(str(customer['date_of_birth']), '%Y%m%d')).days // 365
          # customer['dependants'] = Rand_Gen.get_rand_num(len=1)
          customer['gender'] = Rand_Gen.get_rand_gender(title=customer['title'])
          # customer['title'] = Rand_Gen.get_rand_title(gender=customer['gender'])
          # customer['highest_education_attained'] = Rand_Gen.get_rand_edu()

    if rewrite:
      json_str = json.dumps(customers)
      with open(self.user_db, 'w') as f:
        f.write(json_str)

    logger.info(f"Load user data successful. user data length: {len(customers)}")
    return customers

  def load_trans(self):
    with open(self.trans_db, 'r') as f:
      trans = json.loads(f.read())
      trans = trans['transactions']
    logger.info(f"Load transactions data successful. trans data length: {len(trans)}")
    return trans

  def analysis(self):
    # echart_file = "../data/demo_echart.json"
    # with open(echart_file, 'r') as f:
    #   chart = json.loads(f.read())
    # return chart
    pass


if __name__ == "__main__":
  ana = Analyst(user_db='../data/customer_info.json', trans_db="../data/transactions.json")
  result = ana.analysis()
