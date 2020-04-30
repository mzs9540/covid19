import React, {Component} from "react";
import LineChart from "./LineChart";
import {fetchStats} from "../actions/statsActions";
import {connect} from "react-redux";
import {Typography, Divider, Grid} from "@material-ui/core";
import SideNav from "./SideNav";

class StatsCountry extends Component {

    componentDidMount() {
        this.props.fetchStats(this.props.country);
    }

    componentDidUpdate(prevProps, prevState, snapshot) {
        if (prevProps.country !== this.props.country) {
            this.props.fetchStats(this.props.country);
        }
    }

    render() {
        return(
            <Grid container spacing={0}>
                <Grid item sm={2} key={1}>
                    <SideNav/>
                </Grid>
                <Grid item sm={10} key={2}>
                <Typography variant='h2' align='center'>
                    Past 30 days stats of {this.props.country.toUpperCase()}
                </Typography>
                <Divider/>
                <br/>
                <LineChart
                    stats={{data: this.props.stats.confirmed,
                        title: 'Total Confirmed Cases',
                        labels: this.props.stats.date,
                        label: 'Total Cases',
                    }}/>
                    <br/>
                    <Divider/>
                    <br/>
                <LineChart
                    stats={{data: this.props.stats.recovered,
                        title: 'Total People Recovered',
                        labels: this.props.stats.date,
                        label: 'Recovered',
                    }}/>
                    <br/>
                    <Divider/>
                    <br/>
                <LineChart
                    stats={{data: this.props.stats.deaths,
                        title: 'Total Deaths',
                        labels: this.props.stats.date,
                        label: 'Deaths',}}/>
                </Grid>
            </Grid>
        )
    }
}

const mapStateToProps = state => {
    return {
        stats: state.stats
    }
};

export default connect(mapStateToProps, {fetchStats})(StatsCountry);