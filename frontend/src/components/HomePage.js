import React from "react";

import NewsHelper from "./NewsHelper";
import {Grid} from "@material-ui/core";
import SideNav from "../layouts/SideNav";

class HomePage extends React.Component {

    render() {
        return (
            <Grid container spacing={1}>
                <Grid item sm={2}>
                    <SideNav/>
                </Grid>
                <Grid item sm={10}>
                    <NewsHelper {...this.props}/>
                </Grid>
            </Grid>
        )
    }
}

export default HomePage;