import axios from 'axios';

export default axios.create({
    baseURL: 'http://ec2-18-219-186-53.us-east-2.compute.amazonaws.com:8000'
})