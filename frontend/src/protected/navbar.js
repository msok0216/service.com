import {Nav, Button} from 'react-bootstrap';
import {Link} from 'react-router-dom';
function Navbar() {
    const user = localStorage.getItem('username');
    async function logout() {
        let temp = true;
        console.log('adsfasdf');
        const request = {
            method: 'PUT',
            headers: {'Content-Type': 'application/json', 'token': localStorage.getItem('token')}
        };
        await fetch('/logout', request).then(response =>{   
            localStorage.removeItem('authenticated');
            localStorage.removeItem('username');
            localStorage.removeItem('token');
          if (response.status === 200) {
            console.log('logout');
            temp = false;
          }
        })
        window.location.assign('/');
      // return <Navigate to={'/'}/>;
        // else return 'uee'
      }

    return (
        <Nav className='sidebar flex-column'>
            <Nav.Item className='nav-item'>
                <Nav.Link href={`/dashboard`}>Dashboard</Nav.Link>
            </Nav.Item>
            <Nav.Item className='nav-item'>
                <Nav.Link href={`/post`}>Projects</Nav.Link>
            </Nav.Item>
            <Nav.Item className='nav-item'>
                <Nav.Link href={`/connections`}>Connections</Nav.Link>
            </Nav.Item>
            <Nav.Item className='nav-item'>
                <Nav.Link href={`/profile`}>Profile</Nav.Link>
            </Nav.Item>
            <Nav.Item className='nav-item'>
                <Nav.Link onClick={logout}>Logout</Nav.Link>
            </Nav.Item>
            
        </Nav>
    );
}

export default Navbar;