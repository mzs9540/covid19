import React from "react";

import NewsHelper from "./NewsHelper";
import {Grid} from "@material-ui/core";
import SideNav from "../layouts/SideNav";
import {connect} from "react-redux";
import {fetchNews} from "../actions/newsActions";

class HomePage extends React.Component {

    componentDidMount() {
        this.props.fetchNews();
    }

    render() {
        return (
            <Grid container spacing={0}>
                <Grid item sm={2}>
                    <SideNav/>
                </Grid>
                <Grid item sm={10}>
                    <NewsHelper {...this.props}/>
                </Grid>
            </Grid>
        )
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

export default connect(mapStateToProps, {fetchNews})(HomePage);