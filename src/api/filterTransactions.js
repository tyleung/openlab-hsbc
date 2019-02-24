import axios from 'axios';
import getAllTransactions from './getFirehoseAccounts';

export function filterTransactionsByProductTypes(types) {
    if (!types || !types.length) {
        throw Error('must provide product types.');
    }

    getAllTransactions().then(transactions => {
        // TODO: filter transactions by types
        // types is an array of product types
    });
}