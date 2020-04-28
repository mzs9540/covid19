import React from "react";
import {Container, Fab, TextField} from "@material-ui/core";
import {Field, reduxForm} from "redux-form";
import {connect} from "react-redux";
import {authSignUp} from "../actions";
import {Link} from "react-router-dom";
import Typography from "@material-ui/core/Typography";
import Paper from "@material-ui/core/Paper";

class SignUp extends React.Component{

    renderInput = ({input, type, id, label, margin}) => {
        return (
            <TextField {...input} type={type} id={id} label={label} margin={margin}/>
        )
    };

    onSubmit = (formValues) => {
        this.props.authSignUp(formValues.email, formValues.password, formValues.name);
        this.props.history.push('/');
    };

    render() {
        return(
            <div>
                <Container maxWidth='sm'>
                    <Paper elevation={3} style={{textAlign: 'center', padding: '30px'}}>
                        <Typography variant='h3'>Sign Up</Typography>
                    <form onSubmit={this.props.handleSubmit(this.onSubmit)}>
                        <Field name="name" component={this.renderInput} type="text" id="name"
                               label="Full Name"
                               margin="normal"/>
                        <br/>
                        <Field name="email" component={this.renderInput} type="email" id="email"
                               label="Email"
                               margin="normal"/>
                        <br/>
                        <Field name="password" component={this.renderInput} type="password"
                               id="password"
                               label="Enter Password"
                               margin="normal"/>
                        <br/>
                        <Fab variant="extended" aria-label="Signup" type='submit'>
                            Signup
                        </Fab>
                        or
                        <Link to='/login'>Login</Link>
                    </form>
                    </Paper>
                </Container>
            </div>
        )
    }
}
SignUp = connect(null, {authSignUp})(SignUp);

export default reduxForm({form: 'SignUpForm'})(SignUp);