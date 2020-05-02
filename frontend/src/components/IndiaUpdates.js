import React from "react";
import {connect} from "react-redux";

import NewsHelper from "./NewsHelper";
import {Grid} from "@material-ui/core";
import SideNav from "../layouts/SideNav";
import {fetchNews} from "../actions/newsActions";

class IndiaUpdates extends React.Component {

    componentDidMount() {
        this.props.fetchNews('updates/india');
    }

    render() {
        return (
            <Grid container spacing={0}>
                <Grid item sm={2} key={1}>
                    <SideNav/>
                </Grid>
                <Grid item sm={10} key={2}>
                    <NewsHelper {...this.props}/>
                </Grid>
            </Grid>
        )
    }
}

const mapStateToProps = state => {
    return {
        news: state.news.updates,
        newsError: state.news.error,
        newsLoading: state.news.loading,
        heading: 'Updates by India Gov'
    }
};

export default connect(mapStateToProps, {fetchNews})(IndiaUpdates);