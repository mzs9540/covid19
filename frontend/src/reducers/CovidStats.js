import * as actionTypes from "../actions/types";

const initialState = {
    worldStats: [],
    stats:[],
    deaths: [],
    confirmed: [],
    recovered: [],
    date: [],
    error: null,
    loading: null,
};

const helper = (state, action) => {
    let deaths = [];
    let confirmed = [];
    let recovered = [];
    let date = [];
    action.payload.forEach(stat => {
        deaths.push(stat.deaths);
        confirmed.push(stat.confirmed);
        recovered.push(stat.recovered);
        date.push(stat.date);
    });
    return {...state, worldStats: [],
        stats:[...action.payload],
        deaths: [...deaths],
        confirmed: [...confirmed],
        recovered: [...recovered],
        date: [...date],
        error: null,
        loading: null}
};

const reducer = (state= initialState, action) => {
    switch (action.type) {
        case actionTypes.WORLD_STATS_FETCH_SUCCESS:
            return {...state, worldStats: action.payload, error: null, loading: false};
        case actionTypes.STATS_FETCH_START:
            return {...state, loading: true, error: null};
        case actionTypes.STATS_FETCH_SUCCESS:
            console.log(state);
            return helper(state, action);
        case actionTypes.STATS_FETCH_FAIL:
            return {...state, error: action.payload, loading: false};
        default:
            return state
    }
};

export default reducer;