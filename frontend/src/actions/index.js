import * as actionTypes from './types';

import * as axios from 'axios';


export const authStart = () => {
    return {
        type: actionTypes.AUTH_START
    }
};

export const authSuccess = (token, username) => {
    return {
        type: actionTypes.AUTH_SUCCESS,
        payload: {
            username,
            token
        }
    }
};

export const authFail = err => {
    return {
        type: actionTypes.AUTH_FAIL,
        payload: err
    }
};

export const authLogin = (email, password) => {
    return async dispatch => {
        dispatch(authStart());
        try {
            const res = await axios.post('http://localhost:8000/api/user/token/', {
                email,
                password
            });
            const token = res.data.token;
            localStorage.setItem('token', token);
            localStorage.setItem('username', email);
            dispatch(authSuccess(token, email));
        } catch(err) {
            dispatch(authFail(err));
        }
    }
};

export const authSignUp = (email, password, name) => {
    return async dispatch => {
        try {
            const res = await axios.post('http://localhost:8000/api/user/create/', {
                email,
                password,
                name
            });
            const token = res.data.key;
            localStorage.setItem('token', token);
            dispatch(authSuccess(token, email))
        } catch (e) {
            dispatch(authFail(e))
        }

    }

};

export const authLogout = () => {
    return async dispatch => {
        await axios.get('http://localhost:8000/api/user/logout', {
            headers: {
                Authorization: `Token ${localStorage.getItem('token')}`,
                'Content-Type': 'application/json'
            }
        });
        localStorage.removeItem('token');
        localStorage.removeItem('username');
        dispatch(() => {
            return {
                type: actionTypes.AUTH_LOGOUT
            }
        })
    }
};

export const authCheckLogin = () => {
    return dispatch => {
        const token = localStorage.getItem('token');
        const name = localStorage.getItem('username');
        if (token === undefined) {
            dispatch(authLogout());
        } else {
            dispatch(authSuccess(token, name));
        }
    }
};