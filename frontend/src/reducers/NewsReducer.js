import * as actionTypes from "../actions/types";

const initialState = {
    whoNews: [],
    updates: [],
    error: null,
    loading: null,
};

const reducer = (state= initialState, action) => {
    switch (action.type) {
        case actionTypes.UPDATES_FETCH_SUCCESS:
            return {...state, loading: false, error: null, updates: action.payload};
        case actionTypes.NEWS_FETCH_START:
            return {...state, loading: true};
        case actionTypes.NEWS_FETCH_SUCCESS:
            return {...state, whoNews: action.payload, loading: false, error: null};
        case actionTypes.NEWS_FETCH_FAIL:
            return {...state, error: action.payload, loading: false};
        default:
            return state
    }
};

export default reducer;