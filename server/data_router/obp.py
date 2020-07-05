
import requests

from default import BASE_URL, API_VERSION, BANKS, CONTENT_JSON, DL_TOKEN

class OBP(object):

    # @classmethod
    # def direct_login(token):

    #     login_url = f''

    @classmethod
    def merge_headers(cls, x, y):
        z = x.copy()
        z.update(y)
        return z

    @classmethod
    def get_customers(cls):
        
        customers = {}
        for bank_id in BANKS:
            response = requests.get(f'{BASE_URL}/obp/{API_VERSION}/banks/{bank_id}/firehose/customers', cls.merge_headers(CONTENT_JSON, DL_TOKEN))
            if response:
                customers[bank_id] = response.json()['customers']
        return customers

    @classmethod
    def get_accounts(cls):

        accounts = {}
        for bank_id in BANKS:
            response = requests.get(f'{BASE_URL}/obp/{API_VERSION}/banks/{bank_id}/firehose/accounts/views/owner', cls.merge_headers(CONTENT_JSON, DL_TOKEN))
            if response:
                accounts[bank_id] = response.json()['accounts']

        return accounts

    @classmethod
    def get_transactions_by_account(cls, bank_accounts: dict):
        
        transactions = []

        for bank_id, accounts in bank_accounts.items():
            for account_id in accounts:
                response = requests.get(f'{BASE_URL}/obp/{API_VERSION}/banks/{bank_id}/firehose/accounts/{account_id}//views/owner/transactions', cls.merge_headers(CONTENT_JSON, DL_TOKEN))
                if response:
                    transactions.extend(response.json()['transactions'])

        return transactions

# if __name__ == '__main__':

#     print(OBP.get_customers())