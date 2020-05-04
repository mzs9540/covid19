import React from "react";
import {Container, Paper, Typography, Divider} from "@material-ui/core";

const NewsHelper = (props) => {

    return (
        <Container maxWidth="md">
            <Typography variant='h3' align='center'>
                {props.heading}
            </Typography>
            <Divider/>
            <br/>
            {
                props.news ?
                props.news.map((temp, index) => {
                    return (
                        <div key={index}>
                            <a href={temp.href} target='_blank'
                               rel="noreferrer noopener" style={{textDecoration: "none"}}>
                                <Paper elevation={3} style={{padding: '10px'}}>
                                    <Typography variant='body1'>
                                        {temp.title}
                                    </Typography>
                                    <Divider/>
                                    <Typography variant='body2'>
                                        Published: {temp.date}
                                    </Typography>
                                </Paper>
                            </a>
                            <br/>
                        </div>
                    )
                }) : null
            }
        </Container>
    )
};


export default NewsHelper;