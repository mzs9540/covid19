import { combineReducers } from "redux";
import AuthReducer from './AuthReducer';
import { reducer as formReducer } from "redux-form";
import NewsReducer from "./NewsReducer";
import CovidStats from "./CovidStats";

export default combineReducers({
    auth: AuthReducer,
    form: formReducer,
    news: NewsReducer,
    stats: CovidStats,
});