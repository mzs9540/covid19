import React, {Component} from "react";
import LineChart from "../layouts/LineChart";
import {fetchStats} from "../actions/statsActions";
import {connect} from "react-redux";
import {Typography, Divider} from "@material-ui/core";
import Paper from "@material-ui/core/Paper";

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
            <>
                {/*<Paper>*/}
                {/*    deaths: {this.props.stats.deaths[this.props.stats.deaths.length - 1]},*/}
                {/*    confirmed: {this.props.stats.confirmed[this.props.stats.confirmed.length - 1]},*/}
                {/*    recovered: {this.props.stats.recovered[this.props.stats.recovered.length - 1]},*/}
                {/*    date: {this.props.stats.date[this.props.stats.date.length - 1]}*/}
                {/*</Paper>*/}
                <Typography variant='h2' align='center'>
                    Covid19 Stats of {this.props.country.toUpperCase()}
                </Typography>
                <Divider/>
                <br/>
                <LineChart
                    stats={{data: this.props.stats.confirmed,
                        title: 'Total Confirmed Cases',
                        labels: this.props.stats.date,
                        label: 'Total Cases',
                        backgroundColor: 'rgba(0,255,255,0.2)',
                        color: 'rgb(0,255,255)'
                    }}/>
                    <br/>
                    <Divider/>
                    <br/>
                <LineChart
                    stats={{data: this.props.stats.recovered,
                        title: 'Total People Recovered',
                        labels: this.props.stats.date,
                        label: 'Recovered',
                        backgroundColor: 'rgba(127,255,0,0.2)',
                        color: 'rgb(127,255,0)'
                    }}/>
                    <br/>
                    <Divider/>
                    <br/>
                <LineChart
                    stats={{data: this.props.stats.deaths,
                        title: 'Total Deaths',
                        labels: this.props.stats.date,
                        label: 'Deaths',
                        backgroundColor: 'rgba(255,69,0,0.2)',
                        color: 'rgb(255,69,0)'
                    }}
                />
        </>
        )
    }
}

const mapStateToProps = state => {
    return {
        stats: state.stats
    }
};

export default connect(mapStateToProps, {fetchStats})(StatsCountry);