import axios from 'axios';

// Sends the map click location to the server and gets the nearby transactions in return
export const getTransactionsAroundLocation = latlng => {
  return axios
    .get(`/todo`, {
      data: { latlng }
    })
    .then(response => response.data)
    .catch(error => {
      console.log(error);
    });
};
