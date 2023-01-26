import './login.css';
import Button from 'react-bootstrap/Button';
import Form from 'react-bootstrap/Form';
import { useState } from 'react';
import {Link, Navigate} from 'react-router-dom';

function Login({confirmUsername}) {
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');
    const [error, setError] = useState(false);
    const message = "Either email or password is invalid";

    function handleUsername(event) {
        setUsername(event.target.value);
    }

    function handlePassword(event) {
        setPassword(event.target.value);
    }

    function submit() {
      const request = {
          method: 'PUT',
          headers: {'Content-Type': 'application/json'},
          body: JSON.stringify({
              username: username,
              password: password
          })
      };
      fetch('/login', request).then(response =>{
        if (response.status === 200) {
          // setVerified(true);
          localStorage.setItem('authenticated', true);
        }
        else setError(true);
        return response.json();
      }).then(data => {
        if (data['token'] && data['username']) {
          // setToken(data['token']);
          confirmUsername(data['username']);
          localStorage.setItem('token', data['token']);
          // localStorage.setItem('username', data['username']);
          // console.log(localStorage.getItem('username'))
        } else setError('Unknown Error Occurred');
      });
    }

    if (localStorage.getItem('authenticated') && localStorage.getItem('token')) return <Navigate to={'/dashboard'}/>;
    return (
    <div className="login">
        <Form>
      <Form.Group className="mb-3" controlId="formBasicEmail">
        <Form.Label>Username</Form.Label>
        <Form.Control type="text" placeholder="Enter Username" value={username} onChange={handleUsername}/>
      </Form.Group>

      <Form.Group className="mb-3" controlId="formBasicPassword">
        <Form.Label>Password</Form.Label>
        <Form.Control type="password" placeholder="Password" onChange={handlePassword}/>
      </Form.Group>
      {error && <p className='error'>{message}</p>}
      <Button className="button" variant="primary" type="button" onClick={submit}>
        Submit
      </Button>
        Do not have any account?
        <Link to='/register' className="register-link">Register</Link>
    </Form>
        
        
    </div>
    );
}

export default Login;