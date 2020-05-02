import * as actionTypes from './types';

import awsApi from "../api/awsApi";


const statsFetchStart = () => {
    return {
        type: actionTypes.STATS_FETCH_START
    }
};

const statsFetchSuccess = stats => {
    return {
        type: actionTypes.STATS_FETCH_SUCCESS,
        payload: stats
    }
};

const statsFetchFail = err => {
    return {
        type: actionTypes.STATS_FETCH_FAIL,
        payload: err
    }
};

export const fetchStats = (stats) => {
    return async dispatch => {
        dispatch(statsFetchStart());
        try {
            const res = await awsApi.get(`/api/stats/${stats}`);
                dispatch(statsFetchSuccess(res.data));
        } catch(err) {
            dispatch(statsFetchFail(err));
        }
    }
};