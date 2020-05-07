import * as actionTypes from "../actions/types";

const initialState = {
    mapData: [],
    lon: [],
    lat:[],
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
    let lat = [];
    let lon = [];
    action.payload.forEach(stat => {
        deaths.push(stat.deaths);
        confirmed.push(stat.confirmed);
        recovered.push(stat.recovered);
        date.push(stat.date);
        lat.push(stat.lat);
        lon.push(stat.lon);
    });
    return {...state,
        deaths: [...deaths],
        confirmed: [...confirmed],
        recovered: [...recovered],
        date: [...date],
        lat: [...lat],
        lon: [...lon],
        error: null,
        loading: null}
};


const reducer = (state= initialState, action) => {
    switch (action.type) {
        case actionTypes.MAP_FETCH_SUCCESS:
            return helper(state, action);
        case actionTypes.MAP_FETCH_START:
            return {...state, loading: true, error: null};
        case actionTypes.MAP_FETCH_FAIL:
            return {...state, error: action.payload, loading: false};
        default:
            return state
    }
};

export default reducer;