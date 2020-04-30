import React from 'react';
import { makeStyles } from '@material-ui/core/styles';
import Table from '@material-ui/core/Table';
import {TableBody, Divider} from '@material-ui/core';
import TableCell from '@material-ui/core/TableCell';
import TableContainer from '@material-ui/core/TableContainer';
import TableHead from '@material-ui/core/TableHead';
import TableRow from '@material-ui/core/TableRow';
import Paper from '@material-ui/core/Paper';
import Typography from "@material-ui/core/Typography";

const useStyles = makeStyles({
    table: {
        width: '100%',
    },
});

export default function DenseTable(props) {
    const classes = useStyles();

    return (
        <TableContainer component={Paper}>
            <Typography variant='h3' align='center'>Covid19 World Stats by Worldometer</Typography>
            <Divider/>
            <Divider/>
            <br/>
            <Table className={classes.table} size="small" aria-label="Covid19 Stats">
                <TableHead>
                    <TableRow color='inherit' style={{backgroundColor: 'gray'}}>
                        <TableCell >Country</TableCell>
                        <TableCell align="right">Total Case</TableCell>
                        <TableCell align="right" style={{backgroundColor: 'red'}}>New Case</TableCell>
                        <TableCell align="right">Total Recovered</TableCell>
                        <TableCell align="right">Active Case</TableCell>
                        <TableCell>Cases Per Million</TableCell>
                        <TableCell align="right">Deaths Per Million</TableCell>
                        <TableCell align="right">Total Deaths</TableCell>
                        <TableCell align="right">New Deaths</TableCell>
                    </TableRow>
                </TableHead>
                <TableBody>
                    {props.stats.map((row) => (
                        <TableRow key={row.id}>
                            <TableCell component="th" scope="row">
                                {row.country}
                            </TableCell>
                            <TableCell align="right">{row.total_case}</TableCell>
                            <TableCell align="right" style={{backgroundColor: 'red'}}>
                                {row.new_case}</TableCell>
                            <TableCell align="right">{row.total_recovered}</TableCell>
                            <TableCell align="right">{row.active_case}</TableCell>
                            <TableCell align="right">{row.cases_per_million}</TableCell>
                            <TableCell align="right">{row.deaths_per_million}</TableCell>
                            <TableCell align="right">{row.total_death}</TableCell>
                            <TableCell align="right">{row.new_death}</TableCell>
                        </TableRow>
                    ))}
                </TableBody>
            </Table>
            <br/>
        </TableContainer>
    );
}
