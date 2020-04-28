import React, {Component} from "react";
import {List, ListItem, ListItemIcon, ListItemText, Typography} from "@material-ui/core";
import MailIcon from "@material-ui/icons/Mail";
import history from "../history";


class SideNav extends Component {
    root = {
        background: 'white',
        position: 'sticky',
        bottom: 20,
        zIndex: 5,
    };

    render() {
        return (
            <>
                <br/>
                <br/>
                <br/>
                <div style={this.root}>
                <Typography variant='h5' align='center'>
                    Useful Links
                </Typography>
                <List>
                        <ListItem button key={1} onClick={() => history.push('/who-news')}>
                            <ListItemIcon><MailIcon /></ListItemIcon>
                            <ListItemText primary={'News by WHO'} />
                        </ListItem>
                </List>
                </div>
            </>
        )
    }
}

export default SideNav;