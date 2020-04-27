import * as actionTypes from './types';

import * as axios from 'axios';


export const newFetchStart = () => {
    return {
        type: actionTypes.NEWS_FETCH_START
    }
};

export const newsFetchSuccess = news => {
    return {
        type: actionTypes.NEWS_FETCH_SUCCESS,
        payload: news
    }
};

export const newsFetchFail = err => {
    return {
        type: actionTypes.NEWS_FETCH_FAIL,
        payload: err
    }
};

export const fetchNews = () => {
    return async dispatch => {
        dispatch(newFetchStart());
        try {
            const res = await axios.get('http://localhost:8000/api/news/who-news');
            dispatch(newsFetchSuccess(res.data));
        } catch(err) {
            dispatch(newsFetchFail(err));
        }
    }
};