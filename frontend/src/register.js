import './login.css';
import Button from 'react-bootstrap/Button';
import Form from 'react-bootstrap/Form';
import { useState } from 'react';
import { Alert } from 'react-bootstrap';
import {Link, Navigate} from 'react-router-dom';

function Register() {
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');
    const [confirmPassword, setConfirmPassword] = useState('');
    const [username, setUsername] = useState('');
    const [error, setError] = useState(null);
    const [registered, setRegistered] = useState(false);

    function handleEmail(event) {
        setEmail(event.target.value);
    }

    function handlePassword(event) {
        setPassword(event.target.value);
    }

    function handleConfirmPassword(event) {
        setConfirmPassword(event.target.value);
    }

    function handleUsername(event) {
        setUsername(event.target.value);
    }

    function submit() {
        const request = {
            method: 'PUT',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify({
                email: email,
                username: username,
                password: password,
                confirmPassword: confirmPassword,
            })
        };
        fetch('/register', request).then((response) => {
            if (response.status === 201) {
                console.log('Account is successfully registered');
                setRegistered(true);
            } else {
                return response.json();
            }
        }).then((data) => {
            if (data['error']) {
                console.log(data['error']);
                setError(data['error']);
            }
        });
        // setVerified(true);
    }

    if (registered) return <Navigate to='/'/>;
    return (
    <div className="register">
        <Form>
            <Form.Group className="mb-3" controlId="formId">
                <Form.Label>Username</Form.Label>
                <Form.Control type="text" placeholder="Enter Username" value={username} onChange={handleUsername}/>
            </Form.Group>
            
            <Form.Group className="mb-3" controlId="formBasicEmail">
                <Form.Label>Email address</Form.Label>
                <Form.Control type="email" placeholder="Enter email" value={email} onChange={handleEmail}/>
            </Form.Group>

            <Form.Group className="mb-3" controlId="formBasicPassword">
                <Form.Label>Password</Form.Label>
                <Form.Control type="password" placeholder="Enter Password" onChange={handlePassword}/>
            </Form.Group>

            <Form.Group className="mb-3" controlId="formConfirmPassword">
                <Form.Label>Confirm Password</Form.Label>
                <Form.Control type="password" placeholder="Confirm Password" onChange={handleConfirmPassword}/>
            </Form.Group>
            {error && <p>{error}</p>}
            <Button className="button" variant="primary" type="button" onClick={submit}>
                Register
            </Button>
            Go Back to <Link to='/' className="login-link">Login</Link>
        
        </Form>
    </div>
    );
}

export default Register;