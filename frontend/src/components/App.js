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
            </Router>
        );
    }
}

export default connect(null, {authCheckLogin})(App);