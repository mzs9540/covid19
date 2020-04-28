import React from "react";
import {Container, Paper, Typography, Divider} from "@material-ui/core";

const NewsHelper = (props) => {

    const news = props.location.pathname === '/' ? props.news.slice(0,5) : props.news;

    return (
        <Container maxWidth="md">
            <Typography variant='h3' align='center'>
                {props.heading}
            </Typography>
            <Divider/>
            <br/>
            {
                news.map((temp, index) => {
                    return (
                        <>
                            <a href={temp.href} target='_blank'
                               rel="noreferrer noopener" style={{textDecoration: "none"}}>
                                <Paper key={index} style={{padding: '10px', backgroundColor: "#c8e6c9"}}>
                                    <Typography variant='h6'>
                                        {temp.title}
                                    </Typography>
                                    <Divider/>
                                    <Typography variant='subtitle1'>
                                        Published: {temp.date}
                                    </Typography>
                                </Paper>
                            </a>
                            <br/>
                        </>
                    )
                })
            }
        </Container>
    )
};


export default NewsHelper;