import React, { Component } from 'react';
import {Router, Route} from 'react-router-dom';

import NavBar from "../layouts/Navbar";
import Login from './Login';
import history from "../history";
import SignUp from "./SignUp";


class App extends Component {
    render() {
        return (
            <Router history={history}>
            <NavBar/>
            <Route path='/login' exact component={Login}/>
            <Route path='/sign-up' exact component={SignUp}/>
            </Router>
        );
    }
}

export default App;