import * as actionTypes from "../actions/types";

const initialState = {
    worldStats: [],
    keys: [],
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
        stats:deleteKey(action.payload, 'id'),
        deaths: [...deaths],
        confirmed: [...confirmed],
        recovered: [...recovered],
        date: [...date],
        keys: getKeys(action.payload[0]),
        error: null,
        loading: null}
};

const deleteKey = (arrObj, key) => {
    let arr = arrObj.map(obj => {
        delete obj[key];
        return obj
    });
    return arr
};

const getKeys = obj => {
    return Object.keys(obj).map(str => str.split("_").join(" ").toUpperCase())
};

const reducer = (state= initialState, action) => {
    switch (action.type) {
        case actionTypes.WORLD_STATS_FETCH_SUCCESS:
            return {...state, worldStats: deleteKey(action.payload, 'id'),
                error: null, loading: false, keys: getKeys(action.payload[0])};
        case actionTypes.STATS_FETCH_START:
            return {...state, loading: true, error: null};
        case actionTypes.STATS_FETCH_SUCCESS:
            return helper(state, action);
        case actionTypes.STATS_FETCH_FAIL:
            return {...state, error: action.payload, loading: false};
        default:
            return state
    }
};

export default reducer;