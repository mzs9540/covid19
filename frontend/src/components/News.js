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
        console.log(this.props.news);
        return (
            <Grid container spacing={0}>
                <Grid item sm={3} key={1}>
                    <SideNav/>
                </Grid>
                <Grid item sm={9} key={2}>
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