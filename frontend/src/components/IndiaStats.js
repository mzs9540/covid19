import React from "react";

import NewsHelper from "./NewsHelper";
import {Grid} from "@material-ui/core";
import SideNav from "../layouts/SideNav";
import {connect} from "react-redux";
import Table from '../layouts/Table';
import Divider from "@material-ui/core/Divider";

import StatsCountry from "./StatsCountry";
import {fetchTable} from "../actions/tableActions";
import {fetchStats} from "../actions/statsActions";
import {fetchNews} from "../actions/newsActions";

class IndiaStats extends React.Component {

    componentDidMount() {
        this.props.fetchNews('who-news');
        this.props.fetchTable('india-stats');
        this.props.fetchStats('india');
        this.props.fetchNews('updates/india')
    }

    render() {
        return (
            <Grid container spacing={0}>
                <Grid item sm={2}>
                    <SideNav/>
                </Grid>
                <Grid item sm={9} style={{marginLeft: "auto"}}>
                    <Table stats={this.props.stats.tableData}
                           keys={this.props.stats.keys} title={'State wise Covid19 Data - India'}/>
                    <br/>
                    <Divider/>
                    <br/>
                    <StatsCountry country={'india'}/>
                    <br/>
                    <Divider/>
                    <br/>
                    <NewsHelper news={this.props.news.updates.slice(0, 15)}
                                heading={'Updates by Indian Government'}/>
                </Grid>
            </Grid>
        )
    }
}

const mapStateToProps = state => {
    return {
        news: state.news,
        stats: state.stats,
    }
};

export default connect(mapStateToProps, {fetchNews, fetchTable, fetchStats})(IndiaStats);