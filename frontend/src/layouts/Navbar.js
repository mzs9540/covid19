import React from 'react';
import {AppBar, Toolbar, Typography} from "@material-ui/core";
import SideMenu from "./SideMenu";
import {Link} from "react-router-dom";


class NavBar extends React.Component {

    render() {
        return (
            <>
                <AppBar position='fixed' style={{backgroundColor: '#66bb6a  '}}>
                    <Toolbar >
                        <Link to='/' style={{textDecoration: "none"}}>
                        <Typography variant="h5" style={{color: 'white'}}
                                    align='center'>
                            Covid19
                            <br/>
                            <Typography variant='subtitle2'>
                                Together We Fought, Together We Won
                            </Typography>
                        </Typography>
                        </Link>
                        <hr/>
                        <SideMenu/>
                    </Toolbar>
                </AppBar>
            </>
        )
    }
}


export default NavBar;