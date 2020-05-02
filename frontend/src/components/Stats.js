import React, {Component} from "react";
import {fetchTable} from "../actions/tableActions";
import {connect} from "react-redux";
import Table from '../layouts/Table'
import {Grid} from "@material-ui/core";
import SideNav from "../layouts/SideNav";

class Stats extends Component {

    componentDidMount() {
        this.props.fetchTable('world');
    }

    render() {
        return (
            <Grid container spacing={0}>
                <Grid item sm={2} key={1}>
                    <SideNav/>
                </Grid>
                <Grid item sm={9} key={2} style={{marginLeft: "auto"}}>
                    <Table stats={this.props.stats} keys={this.props.keys}
                           title={'Covid19 Stats by Worldometer'}/>
                </Grid>
            </Grid>
        )
    }
}

const mapStateToProps = state => {
    return {
        stats: state.stats.tableData,
        keys: state.stats.keys,
    }
};

export default connect(mapStateToProps, {fetchTable})(Stats);