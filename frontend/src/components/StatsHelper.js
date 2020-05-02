import React from "react";
import StatsCountry from "./StatsCountry";
import {Grid} from "@material-ui/core";
import SideNav from "../layouts/SideNav";

const statsHelper = (props) => {
    return (
        <Grid container spacing={0}>
            <Grid item sm={2} key={1}>
                <SideNav/>
            </Grid>
            <Grid item sm={10} key={2}>
                <StatsCountry country={props.match.params.country}/>
            </Grid>
        </Grid>
    )
};

export default statsHelper;