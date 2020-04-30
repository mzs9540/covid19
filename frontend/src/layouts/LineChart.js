import React, {Component} from "react";
import {Line} from 'react-chartjs-2';
import {Container, Paper} from "@material-ui/core";


class LineChart extends Component {

    render() {
        return (
            <Container maxWidth='md'>
                <Paper elevation={3}>
                    <Line
                        data={{
                            labels: this.props.stats.labels,
                            datasets: [
                                {
                                    label: this.props.stats.label,
                                    fill: false,
                                    lineTension: 0.5,
                                    borderColor: 'white',
                                    borderWidth: 2,
                                    data: this.props.stats.data,
                                }
                            ]
                        }}
                        options={{
                            backgroundColor: "#424242",
                            title:{
                                display:true,
                                text: this.props.stats.title,
                                fontSize:20,
                                fontColor: '#fff'
                            },
                            label: {
                                fontColor: '#fff'
                            },
                            legend:{
                                display:true,
                                position:'bottom',
                                fontColor: '#fff',
                                labels: {
                                    fontColor: '#fff'
                                }
                            },
                            scales: {
                                yAxes: [{
                                    ticks: {
                                        fontColor: '#fff'
                                    },
                                }],
                                xAxes: [{
                                    ticks: {
                                        fontColor: '#fff'
                                    },
                                }]
                            }
                        }}
                    />
                </Paper>
            </Container>
        );
    }
}


export default LineChart;