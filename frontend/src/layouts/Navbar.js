import React from 'react';
import {AppBar, Toolbar, Typography} from "@material-ui/core";
import SideMenu from "./SideMenu";
import {Link, Router} from "react-router-dom";
import {connect} from "react-redux";


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
                            <Typography variant='srOnly'>
                                Together We Fought, Together We Won
                            </Typography>
                        </Typography>
                        </Link>
                        <hr/>
                        {
                            this.props.isAuth ? <Typography variant='subtitle2'>
                                {this.props.username}
                            </Typography> : null


                        }
                        <SideMenu/>
                    </Toolbar>
                </AppBar>
                <br/>
                <br/>
                <br/>
                <br/>
            </>
        )
    }
}

const mapStateToProps = state => {
    return {
        isAuth: state.auth.token !== null,
        username: state.auth.username
    }
};

export default connect(mapStateToProps)(NavBar);