import React, {Component} from "react";
import {List, ListItem, ListItemText, Typography} from "@material-ui/core";
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
                        <ListItemText primary={'News by WHO'} />
                    </ListItem>
                    <ListItem button key={1} onClick={() => history.push('/stats')}>
                        <ListItemText primary={'Covid19 World Stats'} />
                    </ListItem>
                </List>
                </div>
            </>
        )
    }
}

export default SideNav;