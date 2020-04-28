import React, {Component} from "react";
import {List, ListItem, ListItemText, Typography} from "@material-ui/core";
import history from "../history";


class SideNav extends Component {
    root = {
        background: '#c8e6c9',
        position: 'sticky',
        padding: 30,
        top: 90,
        bottom: 20,
        zIndex: 5
    };

    render() {
        return (
            <div style={this.root}>
                <Typography variant='h5' align='center'>
                    Useful Links
                </Typography>
                <List>
                    <ListItem button key={1} onClick={() => history.push('/who-news')}>
                        <ListItemText primary={'News by WHO'} />
                    </ListItem>
                    <ListItem button key={1} onClick={() => history.push('/stats')}>
                        <ListItemText primary={'Covid19 World Stats'} />
                    </ListItem>
                </List>
            </div>
        )
    }
}

export default SideNav;