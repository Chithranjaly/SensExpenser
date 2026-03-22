import axios from "axios";

const API = axios.create({
    baseURL : "http://127.0.0.1:8000/api/v1",
    withCredentials : true,
});

// signup
export const singup = (data) => API.post("accounts/register/",data);

// signin
export const signin = (data) => API.post("accounts/login/",data);

// logout
export const logout = () => API.post("accounts/logout/")

export default API;