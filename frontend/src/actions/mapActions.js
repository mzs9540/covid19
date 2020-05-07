import * as actionTypes from './types';

import awsApi from "../api/awsApi";


const mapFetchStart = () => {
    return {
        type: actionTypes.MAP_FETCH_START
    }
};

const mapFetchSuccess = map => {
    return {
        type: actionTypes.MAP_FETCH_SUCCESS,
        payload: map
    }
};

const mapFetchFail = err => {
    return {
        type: actionTypes.MAP_FETCH_FAIL,
        payload: err
    }
};

export const fetchMap = (map) => {
    return async dispatch => {
        dispatch(mapFetchStart());
        try {
            const res = await awsApi.get(`/api/stats/${map}`);
            dispatch(mapFetchSuccess(res.data));
        } catch(err) {
            dispatch(mapFetchFail(err));
        }
    }
};