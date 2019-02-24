import axios from 'axios';

export function getFirehoseAccounts() {
    return axios.get("/v3.0.0/banks/hsbc.02.hk.hsbc/firehose/accounts/views/owner", {
        headers: {
            Authorization: `DirectLogin token="eyJhbGciOiJIUzI1NiJ9.eyIiOiIifQ.8FcOstmReHMHIgi18nJCe_FIX2Pfic4_VizrYL2uEBg"`
        }
    }).then(response => {
        if(response && response.status == 200) {
            return response.data
        }
    });
};

export function getFirehoseTransactionsForAccount(accountId) {
    return axios.get(`/v3.0.0/banks/hsbc.02.hk.hsbc/firehose/accounts/${accountId}/views/owner/transactions`, {
        headers: {
            Authorization: `DirectLogin token="eyJhbGciOiJIUzI1NiJ9.eyIiOiIifQ.8FcOstmReHMHIgi18nJCe_FIX2Pfic4_VizrYL2uEBg"`
        }
    }).then(response => {
        if(response && response.status == 200) {
            return response.data
        }
    });
}

export function getAllTransactionData() {
    // just return the mock transaction data
    // return [];
}

// getFirehoseAccounts().then(data => {
//     data.accounts.forEach(account => {
//         console.log(account.id);
//     })
// })

// getFirehoseTransactionsForAccount("5e420e0e-f2ce-4f03-a67c-a1075343dc24").then(data => {
    // console.log(data);
// })