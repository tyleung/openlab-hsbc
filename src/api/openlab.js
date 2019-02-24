import axios from 'axios';

let openlab = axios.create({
    // baseURL: 'https://openlab.openbankproject.com/',
    timeout: 1000,
    // headers: {
    //     'Content-Type': 'application/json',
    //     'Authorization': 'DirectLogin token="eyJhbGciOiJIUzI1NiJ9.eyIiOiIifQ.8FcOstmReHMHIgi18nJCe_FIX2Pfic4_VizrYL2uEBg"'
    // },
    headers: {
        Authorization: `DirectLogin token="eyJhbGciOiJIUzI1NiJ9.eyIiOiIifQ.8FcOstmReHMHIgi18nJCe_FIX2Pfic4_VizrYL2uEBg"`
    }
});

export function testApi() {
    return axios.get('/v1.3.0/banks/hsbc.01.hk.hsbc/cards', {
        headers: {
            Authorization: `DirectLogin token="eyJhbGciOiJIUzI1NiJ9.eyIiOiIifQ.8FcOstmReHMHIgi18nJCe_FIX2Pfic4_VizrYL2uEBg"`
        }
    }).then(response => {
        // console.log(response);
    });
}