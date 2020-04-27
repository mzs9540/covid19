import React, {Component} from "react";
import {connect} from 'react-redux';
import {Field, reduxForm} from "redux-form";
import {authLogin} from "../actions";
import {Container, TextField, Fab, Box} from "@material-ui/core";
import history from "../history";
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
            <Container maxWidth='sm'>
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
                    <Fab variant="extended" aria-label="login" type='submit'>
                        Login
                    </Fab>
                </form>
            </Container>
        )
    }
}

Login = connect(null, {authLogin})(Login);

export default reduxForm({form: 'loginForm'})(Login);