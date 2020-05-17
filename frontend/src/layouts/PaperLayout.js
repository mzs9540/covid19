import React from "react";
import {Paper, Typography} from "@material-ui/core";

const PaperLayout = props => {
    return (
        <>
        <Paper elevation={3} variant={"outlined"} square style={{padding: '10px'}}>
            <Typography variant='h5' align='center'>
                <img src='covid-icon.png' alt='img'/> Helpline:</Typography>
            <Typography variant={'h6'} align='center'>
                <a href='tel:011-23978046'> 011-23978046 </a> or <a href='tel:1075'> 1075 </a>
                <br/>
                <a href='mailto:ncov2019@gov.in'> Email: ncov2019@gov.in</a>
            </Typography>
        </Paper>
            <br/>
            </>
    )
};

export default PaperLayout;