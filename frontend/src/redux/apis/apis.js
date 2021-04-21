import axios from 'axios'


const instance = axios.create({
    // baseURL: "http://127.0.0.1:8000"
    baseURL: "https://netback.herokuapp.com"

})

export default instance