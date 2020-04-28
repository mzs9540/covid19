import React, {Component} from "react";
import {fetchStats} from "../actions/statsActions";
import {connect} from "react-redux";
import Table from '../layouts/Table'
import {Grid} from "@material-ui/core";
import SideNav from "../layouts/SideNav";

class Stats extends Component {

    componentDidMount() {
        this.props.fetchStats();
    }

    render() {
        return (
            <Grid container spacing={1}>
                <Grid item sm={2} key={1}>
                    <SideNav/>
                </Grid>
                <Grid item sm={10} key={2}>
                    <Table stats={this.props.stats}/>
                </Grid>
            </Grid>
        )
    }
}

const mapStateToProps = state => {
    return {
        stats: state.stats.worldStats
    }
};

export default connect(mapStateToProps, {fetchStats})(Stats);