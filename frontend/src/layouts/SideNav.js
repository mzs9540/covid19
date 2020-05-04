import React, {Component} from "react";
import {List, ListItem, ListItemText, Typography} from "@material-ui/core";
import history from "../history";
import {Divider, Paper} from "@material-ui/core";


class SideNav extends Component {
    root = {
        position: 'sticky',
        padding: 30,
        top: 90,
        bottom: 20,
        zIndex: 5,
        overflowY: 'scroll',
        width:'100%',
    };

    render() {
        return (
            <Paper id='sidenav-scrollbar' elevation={3} style={this.root}>
                <List>
                    <Typography variant='h6' align='center'>
                        Useful Links
                    </Typography>
                    <Divider/>
                    <Divider/>
                    <ListItem button key={15} onClick={() => history.push('/updates/india-full')}>
                        <ListItemText primary={'Updates by Indian Gov.'} />
                    </ListItem>
                    <ListItem button key={1} onClick={() => history.push('/updates/india')}>
                        <ListItemText primary={'India Stats'} />
                    </ListItem>
                    <ListItem button key={2} onClick={() => history.push('/who-news')}>
                        <ListItemText primary={'News by WHO'} />
                    </ListItem>
                    <ListItem button key={14} onClick={() => history.push('/stats')}>
                        <ListItemText primary={'Covid19 World Stats'} />
                    </ListItem>
                    <Divider/>
                    <Divider/>
                    <Typography variant='h6' align='center'>
                        Stats of Countries
                    </Typography>
                    <Divider/>
                    <Divider/>
                    <ListItem button key={3} onClick={() => history.push('/stats/india')}>
                        <ListItemText primary={'India'} />
                    </ListItem>
                    <ListItem button key={4} onClick={() => history.push('/stats/us')}>
                        <ListItemText primary={'United State'} />
                    </ListItem>
                    <ListItem button key={6} onClick={() => history.push('/stats/china')}>
                        <ListItemText primary={'China'} />
                    </ListItem>
                    <ListItem button key={7} onClick={() => history.push('/stats/iran')}>
                        <ListItemText primary={'Iran'} />
                    </ListItem>
                    <ListItem button key={8} onClick={() => history.push('/stats/turkey')}>
                        <ListItemText primary={'Turkey'} />
                    </ListItem>
                    <ListItem button key={9} onClick={() => history.push('/stats/germany')}>
                        <ListItemText primary={'Germany'} />
                    </ListItem>
                    <ListItem button key={10} onClick={() => history.push('/stats/spain')}>
                        <ListItemText primary={'Spain'} />
                    </ListItem>
                    <ListItem button key={11} onClick={() => history.push('/stats/france')}>
                        <ListItemText primary={'France'} />
                    </ListItem>
                    <ListItem button key={12} onClick={() => history.push('/stats/russia')}>
                        <ListItemText primary={'Russia'} />
                    </ListItem>
                    <ListItem button key={13} onClick={() => history.push('/stats/ukraine')}>
                        <ListItemText primary={'Ukraine'} />
                    </ListItem>
                </List>
            </Paper>
        )
    }
}

export default SideNav;