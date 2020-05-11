import React from "react";
import {Paper, Typography} from "@material-ui/core";
import {Link} from "react-router-dom";

const PaperLayout = props => {
    return (
        <>
        <Paper elevation={3} variant={"outlined"} square style={{padding: '10px'}}>
            <Typography variant='h5' align='center'>
                <img src='covid-icon.png' alt='img'/> Helpline:</Typography>
            <Typography variant={'h6'} align='center'>
                <Link to='tel:011-23978046'>011-23978046</Link> or <Link to='tel:1075'>1075</Link>
                <Link to='mailto:ncov2019@gov.in'> Email: ncov2019@gov.in</Link>
            </Typography>
        </Paper>
            <br/>
            </>
    )
};

export default PaperLayout;