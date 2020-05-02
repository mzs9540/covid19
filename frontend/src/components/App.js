import React, { Component } from 'react';
import {Route, Router} from "react-router-dom";
import history from "../history";
import Login from "./Login";
import SignUp from "./SignUp";
import HomePage from "./HomePage";
import News from "./News";
import NavBar from "../layouts/Navbar";
import {connect} from "react-redux";
import {authCheckLogin} from "../actions";
import Stats from "./Stats";
import statsHelper from "./StatsHelper";
import IndiaStats from "./IndiaStats";
import IndiaUpdates from "./IndiaUpdates";


class App extends Component {

    componentDidMount() {
        this.props.authCheckLogin();
    }

    render() {
        return (
            <Router history={history}>
                <NavBar/>
                <Route path='/' exact component={HomePage}/>
                <Route path='/who-news' exact component={News}/>
                <Route path='/login' exact component={Login}/>
                <Route path='/sign-up' exact component={SignUp}/>
                <Route path='/stats/' exact component={Stats}/>
                <Route path='/updates/india' exact component={IndiaStats}/>
                <Route path='/updates/india-full' exact component={IndiaUpdates}/>
                <Route path='/stats/:country' exact component={statsHelper}/>
            </Router>
        );
    }
}

export default connect(null, {authCheckLogin})(App);