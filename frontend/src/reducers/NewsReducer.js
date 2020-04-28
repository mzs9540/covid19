import * as actionTypes from "../actions/types";

const initialState = {
    whoNews: [],
    error: null,
    loading: null,
};

const reducer = (state= initialState, action) => {
    switch (action.type) {
        case actionTypes.NEWS_FETCH_START:
            return {...state, loading: true};
        case actionTypes.NEWS_FETCH_SUCCESS:
            return {...state, whoNews: action.payload, loading: false};
        case actionTypes.NEWS_FETCH_FAIL:
            return {...state, error: action.payload, loading: false};
        default:
            return initialState
    }
};

export default reducer;