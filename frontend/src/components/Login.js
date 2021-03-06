import React, {Component} from "react";
import {connect} from 'react-redux';
import {Field, reduxForm} from "redux-form";
import {authLogin} from "../actions";
import {Container, TextField, Fab, Box, Grid} from "@material-ui/core";
import history from "../history";
import SideNav from "../layouts/SideNav";
import Paper from "@material-ui/core/Paper";
import {Typography, Divider} from "@material-ui/core";
import {Link} from "react-router-dom";

class Login extends Component {

    renderInput = ({input, type, id, label,margin}) => {
        return <Box>
            <TextField {...input} label={label}  id={id} margin={margin} type={type}/>
        </Box>
    };

    onSubmit = (values) => {
        this.props.authLogin(values.username, values.password);
        history.push('/')
    };

    render() {
        return (
            <Grid container spacing={1}>
                <Grid item sm={2}>
                    <SideNav/>
                </Grid>
                <Grid item sm={10}>
                    <Container maxWidth='sm'>
                        <Paper className='border-decorate' elevation={3}
                               style={{textAlign: 'center', padding: '30px'}}>
                            <Typography variant='h3'>Login</Typography>
                            <Divider/>
                            <form onSubmit={this.props.handleSubmit(this.onSubmit)}>
                                <Field name="username" component={this.renderInput} type="text" id="username"
                                       label="Username"
                                       margin="normal"/>
                                <br/>
                                <Field name="password" component={this.renderInput} type="password"
                                       id="password"
                                       label="Password"
                                       margin="normal"/>
                                <br/>
                                <Fab variant="extended" aria-label="login" type='submit'
                                     className='button-decorate'>
                                    Login
                                </Fab>
                            </form>
                            <br/>
                            <Divider/>
                            <br/>
                            <Link to='/sign-up'>or Sign Up</Link>
                        </Paper>
                    </Container>
                </Grid>
            </Grid>
        )
    }
}

Login = connect(null, {authLogin})(Login);

export default reduxForm({form: 'loginForm'})(Login);