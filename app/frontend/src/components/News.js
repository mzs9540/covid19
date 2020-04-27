import React from "react";
import {connect} from "react-redux";

import NewsHelper from "./NewsHelper";
import {Grid} from "@material-ui/core";
import SideNav from "../layouts/SideNav";
import {fetchNews} from "../actions/newsActions";

class News extends React.Component {

    componentDidMount() {
        this.props.fetchNews();
    }

    render() {
        return (
            <Grid container spacing={1}>
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
        news: state.news.whoNews,
        newsError: state.news.error,
        newsLoading: state.news.loading,
        heading: 'News Published by WHO'
    }
};

export default connect(mapStateToProps, {fetchNews})(News);