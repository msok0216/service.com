
import './profile.css';
import Navbar from './navbar';
import ProfileContent from './profileContent';
import { useEffect, useState } from 'react';
import * as d3 from 'd3';



function Profile() {
    const [username, setUsername] = useState(null);

    // useEffect(() => {
    //     drawChart(400,600);
    // }, []);

    return (
    <div className='profile-content'>
        {/* <Navbar /> */}
        <ProfileContent/>


        
    </div>
    );
}

export default Profile;