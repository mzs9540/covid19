import * as actionTypes from './types';
import awsApi from "../api/awsApi";


const newFetchStart = () => {
    return {
        type: actionTypes.NEWS_FETCH_START
    }
};

const newsFetchSuccess = news => {
    return {
        type: actionTypes.NEWS_FETCH_SUCCESS,
        payload: news
    }
};

const newsFetchFail = err => {
    return {
        type: actionTypes.NEWS_FETCH_FAIL,
        payload: err
    }
};


const updatesFetchSuccess = data => {
    return {
        type: actionTypes.UPDATES_FETCH_SUCCESS,
        payload: data
    }
};


export const fetchNews = (news) => {
    return async dispatch => {
        dispatch(newFetchStart());
        try {
            const res = await awsApi.get(`/api/news/${news}`);
            if (news === 'who-news') {
                dispatch(newsFetchSuccess(res.data));
            } else {
                dispatch(updatesFetchSuccess(res.data))
            }
        } catch(err) {
            dispatch(newsFetchFail(err));
        }
    }
};