import * as actionTypes from "../actions/types";

const initialState = {
    token: null,
    username: null,
    error: null,
    loading: false
};

const reducer = (state= initialState, action) => {
    switch (action.type) {
        case actionTypes.AUTH_LOGOUT:
            return initialState;
        case actionTypes.AUTH_SUCCESS:
            return {...state, token: action.payload.token,
                username: action.payload.username, loading: false, error: null};
        case actionTypes.AUTH_FAIL:
            return {...state, error: action.payload, loading: false, token: null};
        case actionTypes.AUTH_START:
            return {...state, error: null, loading: true};
        default:
            return initialState

    }
};

export default reducer;