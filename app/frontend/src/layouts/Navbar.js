import React from 'react';
import {AppBar, Toolbar, Typography} from "@material-ui/core";


class NavBar extends React.Component {

    render() {
        return (
            <AppBar position='static' color='secondary'>
                <Toolbar>
                    <Typography variant="h2" color='inherit'>
                        MZS
                    </Typography>
                    <hr/>
                </Toolbar>
            </AppBar>
        )
    }
}


export default NavBar;