import * as actionTypes from './types';

import awsApi from "../api/awsApi";


const tableFetchStart = () => {
    return {
        type: actionTypes.STATS_FETCH_START
    }
};

const tableFetchSuccess = table => {
    return {
        type: actionTypes.TABLE_DATA_FETCH_SUCCESS,
        payload: table
    }
};

const tableWorldFetchSuccess = table => {
    return {
        type: actionTypes.WORLD_TABLE_FETCH_SUCCESS,
        payload: table
    }
};

const tableFetchFail = err => {
    return {
        type: actionTypes.STATS_FETCH_FAIL,
        payload: err
    }
};

export const fetchTable = (table) => {
    return async dispatch => {
        dispatch(tableFetchStart());
        try {
            const res = await awsApi.get(`/api/stats/${table}`);
            if (table === 'world'){
                dispatch(tableWorldFetchSuccess(res.data))
            } else {
                dispatch(tableFetchSuccess(res.data));
            }
        } catch(err) {
            dispatch(tableFetchFail(err));
        }
    }
};