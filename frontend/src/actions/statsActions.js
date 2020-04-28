import * as actionTypes from './types';

import awsApi from "../api/awsApi";


export const statsFetchStart = () => {
    return {
        type: actionTypes.STATS_FETCH_START
    }
};

export const statsFetchSuccess = stats => {
    return {
        type: actionTypes.STATS_FETCH_SUCCESS,
        payload: stats
    }
};

export const statsFetchFail = err => {
    return {
        type: actionTypes.STATS_FETCH_FAIL,
        payload: err
    }
};

export const fetchStats = () => {
    return async dispatch => {
        dispatch(statsFetchStart());
        try {
            const res = await awsApi.get('/api/stats');
            console.log(res);
            dispatch(statsFetchSuccess(res.data));
        } catch(err) {
            dispatch(statsFetchFail(err));
        }
    }
};