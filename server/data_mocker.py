"""
For this module
entry fucntion is transaction_generator(num, output_path)
it's only needed to call transaction_generator, specify the number of transactions we want to genenrate
and the transaction output json file, if not then no output, just return json str
"""

import json
import uuid
import time
import random
from utils.rand_gen import Rand_Gen as RandGen

class TransactionMocker:

    def __init__(self):
        pass

    def this_account(self, id : str = None) -> dict:

        bank_id = RandGen.get_rand_bank_id()
        account = id if id else str(uuid.uuid1())
        # product = products_generator()

        ret = {}
        ret['id'] = id if id else str(uuid.uuid1())
        ret['bank_routing'] = {
            "scheme": bank_id,
            "address": bank_id
        }
        ret['account_routings'] = [{
            "scheme": account,
            "address": account
        }]
        ret['holders'] = [{
            "name": 'this account user',
            "is_alias":True
        }]

        return ret

    def other_account(self, id : str = None) -> dict:

        bank_id = RandGen.get_rand_bank_id()
        account = id if id else str(uuid.uuid1())

        ret = {}
        
        ret['id'] = account
        ret['holders'] = {
            "name": 'target user',
            "is_alias": True
        }
        ret['bank_routing'] = {
            "scheme": bank_id,
            "address": bank_id
        }
        ret['account_routings'] = [{
            "scheme": account,
            "address": account
        }]
        ret['metadata'] = self.meta_data()

        return ret


    def meta_data(self) -> dict:

        coordinates = RandGen.get_rand_geo()

        ret = {
            "product_type": RandGen.get_rand_prod_type(),
            "public_alias": "NONE",
            "private_alias": "NONE",
            "URL": "www.openbankproject.com",
            "location":{
                "latitude": str(coordinates[0]),
                "longitude": str(coordinates[1]),
            }
        }
        return ret

    def details(self) -> dict:

        curr_type = RandGen.get_rand_curr_type()
        time = RandGen.get_rand_time()
        
        ret = {
            "type": RandGen.get_rand_trans_type(),
            "description": "this is for openlab",
            "posted": time,
            "completed": time,
            "new_balance":{
                "currency": curr_type,
                "amount": RandGen.get_rand_amount(is_balance=True)
            },
            "value":{
                "currency": curr_type,
                "amount": RandGen.get_rand_amount(is_balance=False)
            }
        }
        return ret

    def transaction_generator(self, num: int = 10000, output_path: str = '') -> str:

        with open('./data/customer_info.json', 'r') as f:
            ids = [customer['customer_id'] for customer in json.load(f)]
        num_ids = len(ids) - 1

        trans = {
            "transactions": []
        }

        for i in range(num):
            single_trans = {
                "id": str(uuid.uuid1()),
                "this_account": self.this_account(ids[int(random.random()*num_ids)]),
                "other_account": self.other_account(ids[int(random.random()*num_ids)]),
                "details": self.details(),
                "metadata": self.meta_data()
            }
            trans['transactions'].append(single_trans)

        if output_path:
            with open(output_path, 'w') as f:
                json.dump(trans, f)

        return json.dumps(trans)



if __name__ == '__main__':
    num_trans = 10

    trans = TransactionMocker().transaction_generator(num_trans, './data/1.json')
    print(trans)