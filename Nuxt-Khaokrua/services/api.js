// import httpClient from "../services/httpClient";
import { server } from "../services/constants";
import axios from 'axios'

const isLoggedIn = () => {
    const token = localStorage.getItem('USERNAME');
    console.log('isLoggedIN',token)
    return token != null;
};


const logoff = () => {
    localStorage.removeItem('TOKEN');
    localStorage.removeItem('USERNAME');
  };

export default {
    logoff,
    isLoggedIn,
};