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

export const getRealtimeData = options => {
  return axios
    .get(`http://127.0.0.1:5000/realtime_chart?radius=${options.radius}&product_type=${options.product_type}&loc=${options.loc}`)
    .then(response => response.data)
    .catch(error => {
      console.log(error);
    });
};

export const getAreaInfo = options => {
  return axios
    .get(`http://127.0.0.1:5000/get_area_info?x=${options.x}&y=${options.y}`)
    .then(response => response.data)
    .catch(error => {
      console.log(error);
    });
  }