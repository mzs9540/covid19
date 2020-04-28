import * as actionTypes from "../actions/types";

const initialState = {
    worldStats: [],
    error: null,
    loading: null,
};

const reducer = (state= initialState, action) => {
    switch (action.type) {
        case actionTypes.STATS_FETCH_START:
            return {...state, loading: true};
        case actionTypes.STATS_FETCH_SUCCESS:
            return {...state, worldStats: action.payload, loading: false};
        case actionTypes.STATS_FETCH_FAIL:
            return {...state, error: action.payload, loading: false};
        default:
            return state
    }
};

export default reducer;