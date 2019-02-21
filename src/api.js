import axios from 'axios';

export const getCurrentUser = () => {
  return axios
    .get(`/users/current`, {
      headers: {
        Authorization: `DirectLogin token="${
          process.env.REACT_APP_DIRECT_LOGIN_TOKEN
        }"`
      }
    })
    .then(response => response.data)
    .catch(error => {
      console.log(error);
    });
};
