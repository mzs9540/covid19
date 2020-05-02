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
        textAlign: 'center'
    },
});

export default function DenseTable(props) {
    const classes = useStyles();
    return (
        <TableContainer component={Paper}>
            <Typography variant='h3' align='center'>{props.title}</Typography>
            <Divider/>
            <Divider/>
            <br/>
            <Table className={classes.table} size="small" aria-label="Covid19 Stats">
                <TableHead>
                    <TableRow key={'was'} color='inherit' style={{backgroundColor: 'gray'}}>
                        {props.keys ? props.keys.map((key, index) =>
                            <TableCell align='center' key={index}><Typography variant='subtitle2'>{key}</Typography></TableCell>) : null}
                    </TableRow>
                </TableHead>
                <TableBody>

                    {
                        props.stats ?
                            props.stats.map((row, index) => (
                                <TableRow key={index*Math.random()}>
                                    {Object.values(row).map((val,i) =>
                                        <TableCell key={i+val+23} component="th" scope="row" align='center'>
                                            {val}
                                        </TableCell>
                                    )
                                    }
                                </TableRow>
                            )) : null
                    }
                </TableBody>
            </Table>
            <br/>
        </TableContainer>
    );
}
