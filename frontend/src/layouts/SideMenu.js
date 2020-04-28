import React from 'react';
import clsx from 'clsx';
import { makeStyles } from '@material-ui/core/styles';
import {SwipeableDrawer, Button, List, Divider, ListItemText, ListItemIcon, ListItem} from '@material-ui/core';

import MailIcon from '@material-ui/icons/Mail';
import MenuIcon from '@material-ui/icons/Menu';
import history from "../history";

const useStyles = makeStyles({
    list: {
        width: 250,
    }
});

export default function SwipeableTemporaryDrawer() {
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
        >
            <List>
                <ListItem button key={1} onClick={() => history.push('/login')}>
                        <ListItemIcon><MailIcon /></ListItemIcon>
                        <ListItemText primary={'Login'} />
                    </ListItem>
            </List>
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
