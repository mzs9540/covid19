import React from 'react';
import clsx from 'clsx';
import { makeStyles } from '@material-ui/core/styles';
import {SwipeableDrawer, Button, List, Divider, ListItemText, ListItem} from '@material-ui/core';

import MenuIcon from '@material-ui/icons/Menu';
import history from "../history";
import {connect} from "react-redux";
import {authLogout} from "../actions";

const useStyles = makeStyles({
    list: {
        width: 250,
    }
});

function SwipeableTemporaryDrawer(props) {
    const classes = useStyles();
    const [state, setState] = React.useState({
        right: false,
    });

    const toggleDrawer = (anchor, open) => (event) => {
        if (event && event.type === 'keydown' && (event.key === 'Tab' || event.key === 'Shift')) {
            return;
        }

        setState({ ...state, [anchor]: open });
    };

    const list = (anchor) => (
        <div
            className={clsx(classes.list)}
            role="presentation"
            onClick={toggleDrawer(anchor, false)}
            onKeyDown={toggleDrawer(anchor, false)}
        >{
            !props.isAuth ?
            <List>
                <ListItem button key={1} onClick={() => history.push('/login')}>
                    <ListItemText primary={'Login'}/>
                </ListItem>
                <ListItem button key={2} onClick={() => history.push('/sign-up')}>
                    <ListItemText primary={'Sign Up'}/>
                </ListItem>
            </List> :
                <List>
                    <ListItem button key={1} onClick={() => props.authLogout()}>
                        <ListItemText primary={'Logout'}/>
                    </ListItem>
                </List>
        }
            <Divider />
        </div>
    );

    return (
        <React.Fragment key={'right'}>
            <Button onClick={toggleDrawer('right', true)}>
                <MenuIcon/>
            </Button>
            <SwipeableDrawer
                anchor={'right'}
                open={state['right']}
                onClose={toggleDrawer('right', false)}
                onOpen={toggleDrawer('right', true)}
            >
                {list('right')}
            </SwipeableDrawer>
        </React.Fragment>
    );
}

const mapStateToProps = state => {
    return {
        isAuth: state.auth.token !== null
    }
};

export default connect(mapStateToProps, {authLogout})(SwipeableTemporaryDrawer);
