import React from 'react';
import { Fade, Menu, Button, MenuItem} from '@material-ui/core';
import DehazeIcon from '@material-ui/icons/Dehaze';
import {Link} from "react-router-dom";

export const FadeMenu = props => {
    const [anchorEl, setAnchorEl] = React.useState(null);
    const open = Boolean(anchorEl);

    const handleClick = event => {
        setAnchorEl(event.currentTarget);
    };

    const handleClose = () => {
        setAnchorEl(null);
    };

    return (
        <div>
            <Button aria-controls="fade-menu" aria-haspopup="true" color='inherit' onClick={handleClick}>
                <DehazeIcon/>
            </Button>
            <Menu
                id="fade-menu"
                anchorEl={anchorEl}
                keepMounted
                open={open}
                onClose={handleClose}
                TransitionComponent={Fade}
            >
                { props.isAuth ?
                    [
                        <MenuItem onClick={handleClose} key={0}> Welcome {props.username}</MenuItem>,
                        <MenuItem onClick={() => {
                            props.authLogout();
                        }} key={1}>Logout</MenuItem>
                    ]
                    :
                    <MenuItem ><Link to='/login'>Login</Link></MenuItem>
                }
            </Menu>
        </div>
    );
};