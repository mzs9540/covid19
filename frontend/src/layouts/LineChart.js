import React, {Component} from "react";
import {Line} from 'react-chartjs-2';
import {Container, Paper} from "@material-ui/core";


class LineChart extends Component {

    render() {
        return (
            <Container maxWidth='md'>
                <Paper elevation={3} id='LineChart'>
                    <Line
                        data={{
                            labels: this.props.stats.labels,
                            datasets: [
                                {
                                    label: this.props.stats.label,
                                    fill: true,
                                    lineTension: 0.5,
                                    borderColor: this.props.stats.color,
                                    backgroundColor: this.props.stats.backgroundColor,
                                    borderWidth: 2,
                                    data: this.props.stats.data,
                                }
                            ]
                        }}
                        options={{
                            backgroundColor: "rgb(0,0,0)",
                            responsive: true,
                            maintainAspectRatio: false,
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
                                    gridLines: {
                                        zeroLineColor: '#ffcc33'
                                    }
                                }],
                                xAxes: [{
                                    ticks: {
                                        fontColor: '#fff'
                                    },
                                    gridLines: {
                                        zeroLineColor: '#ffcc33'
                                    }
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