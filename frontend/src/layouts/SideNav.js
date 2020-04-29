import React, {Component} from "react";
import {List, ListItem, ListItemText, Typography} from "@material-ui/core";
import history from "../history";
import Divider from "@material-ui/core/Divider";


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
                <Typography variant='h6' align='center'>
                    Useful Links
                </Typography>
                <Divider/>
                <List>
                    <ListItem button key={1} onClick={() => history.push('/who-news')}>
                        <ListItemText primary={'News by WHO'} />
                    </ListItem>
                    <Divider/>
                    <ListItem button key={2} onClick={() => history.push('/stats')}>
                        <ListItemText primary={'Covid19 World Stats'} />
                    </ListItem>
                </List>
            </div>
        )
    }
}

export default SideNav;