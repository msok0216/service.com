import { useState, useEffect } from "react";
import './connections.css';

export default function Connections() {
    const [connections, setConnections] = useState([]);

    function fetchConnectionsData(page) {
        const request = {
            method: 'GET',
            headers: {'Content-Type': 'application/json', 'token': localStorage.getItem('token')}
        };
        fetch('user/connections', request).then(async response => {
            const data = await response.json();
            if (!response.ok) {
                const error = (data && data.message) || response.statusText;
                return Promise.reject(error);
            }
            setConnections(data['connections']);
        }).catch(error => {
            console.error('An error occurred', error);
        });
    }

    useEffect(() => {
        // drawChart(400,600);
        fetchConnectionsData(1);
        // console.log(shifts);

    }, []);

    return (
        <div className="connections-content">
            {
                connections.map(connection => <div key={connection.user}>{connection.user}</div>)
            }
        </div>

    );
}

