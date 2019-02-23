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

random.seed(time.time())

# generate geo coordinates in HK
def geo_generator(hot_points: list = []) -> tuple:
    
    # some hot spots in hk
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

def time_generator(hot_interval: list = None) -> str:
    date = '2018-08-08'
    r = random.random()
    if r < 0.6:
        time = f'{random.randint(10, 18)}:00:00'
    elif r < 0.9:
        time = f'{random.randint(20, 24)}:00:00'
    else:
        sparse_time = ['08', '09', '19', '01']
        time = f'{sparse_time[random.randint(0, 4)]}:00:00'
    return date+'T'+time+'Z'

def bank_id_generator() -> str:

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

def trans_type_generator() -> str:

    trans_types = ['purchase', 'transfer']

    r  = random.random()
    if r < 0.7:
        return trans_types[0]
    else:
        return trans_types[1]

def product_type_generator() -> str:

    product_types = {
        'hot_types': ['Electronics', 'Fashion', 'PersonalCare', 'Movie&Music'],
        'mid_types': ['Softwares', 'Baby', 'Books', 'Household'],
        'cold_types': ['Automotive', 'Pet', 'industrial']
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

def curr_generator() -> str:

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

def amount_generator(is_balance: bool = False) -> str:

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


def this_account(id : str = None) -> dict:

    bank_id = bank_id_generator()
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


def other_account(id : str = None) -> dict:

    bank_id = bank_id_generator()
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
    ret['metadata'] = meta_data()

    return ret


def meta_data() -> dict:

    coordinates = geo_generator()

    ret = {
        "product_type": product_type_generator(),
        "public_alias": "NONE",
        "private_alias": "NONE",
        "URL": "www.openbankproject.com",
        "location":{
          "latitude": str(coordinates[0]),
          "longitude": str(coordinates[1]),
        }
    }
    return ret


def details() -> dict:

    curr_type = curr_generator()
    time = time_generator()
    
    ret = {
      "type": trans_type_generator(),
      "description": "this is for openlab",
      "posted": time,
      "completed": time,
      "new_balance":{
        "currency": curr_type,
        "amount": amount_generator(is_balance=True)
      },
      "value":{
        "currency": curr_type,
        "amount": amount_generator(is_balance=False)
      }
    }
    return ret


def transaction_generator(num: int = 10000, output_path: str = '') -> str:

    with open('./data_mocker/customer_info.json', 'r') as f:
        ids = [customer['customer_id'] for customer in json.load(f)]
    num_ids = len(ids) - 1

    trans = {
        "transactions": []
    }

    for i in range(num):
        single_trans = {
            "id": str(uuid.uuid1()),
            "this_account": this_account(ids[int(random.random()*num_ids)]),
            "other_account": other_account(ids[int(random.random()*num_ids)]),
            "details": details(),
            "metadata": meta_data()
        }
        trans['transactions'].append(single_trans)

    if output_path:
        with open(output_path, 'w') as f:
            json.dump(trans, f)

    return json.dumps(trans)



if __name__ == '__main__':
    num_trans = 10

    trans = transaction_generator(num_trans, './data_mocker/mock_transactions.json')
    print(trans)