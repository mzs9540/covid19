import React, {Component} from "react";
import {Bar} from "react-chartjs-2";
import Paper from "@material-ui/core/Paper";


class BarChart extends Component {
    render() {
        return (
            <Paper elevation={3}>
            <Bar
                data={{
                    labels: ['Confirmed', 'Recovered', 'Deaths'],
                    datasets: [
                        {
                            label: 'People',
                            backgroundColor: ['rgb(0, 255, 255)', 'rgb(127, 255, 0)', 'rgb(255, 69, 0)'],
                            data: [this.props.stats.confirmed,
                                this.props.stats.recovered, this.props.stats.deaths],
                        },
                    ],
                }}
                options={{
                    legend: { display: false },
                    title: { display: true, text: `Current state on ${this.props.stats.date}` },
                }}
            />
            </Paper>
        )
    }
}

export default BarChart;