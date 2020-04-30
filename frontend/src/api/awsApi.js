import axios from 'axios';

const x = 1;
let baseURL = 'http://ec2-18-219-186-53.us-east-2.compute.amazonaws.com:8000';

if (!x) {
    baseURL = 'http://localhost:8000';
}

export default axios.create({
    baseURL: baseURL
})