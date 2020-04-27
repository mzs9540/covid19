import React, { Component } from 'react';
import {Route, Router} from "react-router-dom";
import history from "../history";
import Login from "./Login";
import SignUp from "./SignUp";
import HomePage from "./HomePage";
import News from "./News";
import NavBar from "../layouts/Navbar";
import {connect} from "react-redux";
import {fetchNews} from "../actions/newsActions";



class App extends Component {

    componentDidMount() {
        this.props.fetchNews();
    }

    render() {
        return (
            <>
                <br/>
                <br/>
                <br/>
                <br/>
                <Router history={history}>
                    <NavBar/>
                    <Route path='/' exact render={(props) => <HomePage {...props} {...this.props}/>}/>
                    <Route path='/who-news' exact component={News}/>
                    <Route path='/login' exact component={Login}/>
                    <Route path='/sign-up' exact component={SignUp}/>
                </Router>
            </>
        );
    }
}

const mapStateToProps = state => {
    return {
        news: state.news.whoNews.slice(0, 5),
        newsError: state.news.error,
        newsLoading: state.news.loading,
        heading: 'News by WHO'
    }
};

export default connect(mapStateToProps, {fetchNews})(App);