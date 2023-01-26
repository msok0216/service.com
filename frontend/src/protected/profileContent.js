import * as d3 from 'd3';
// import { Table } from 'react-bootstrap';
import ShiftTable from './profile/ShiftTable';
import { useEffect, useState } from 'react';
// import { geoConicEquidistantRaw } from 'd3';




function ProfileContent() {
    const [graphData, setGraphData] = useState();

    function drawChart(height, width) {
        d3.select('.graph')
            .append("svg")
            .attr("width", width)
            .attr("height", height)
            .style("border", "1px solid black")
            .append("text")
            .attr("fill", "green")
            .attr("x", 50)
            .attr("y", 50)
            .text("Hello")
    
            d3.json(graphData, function(data) {
                // console.log(data);
            })
    }

    function loadData() {
        const request = {
            method: 'GET',
            headers: {'Content-Type': 'application/json', 'token': localStorage.getItem('token')}
        };
        fetch('user/graphdata', request).then(async response => {
            const data = await response.json();
            if (!response.ok) {
                const error = (data && data.message) || response.statusText;
                return Promise.reject(error);
            }
            // console.log(data['shifts'])
            setGraphData(data['shifts']);
        }).catch(error => {
            console.error('An error occurred', error);
        });
        // console.log(page);
    }



    useEffect(() => {
        loadData();
        drawChart(400,600);
    }, []);

    return (
        <div>

            <div className='graph'>
            </div>
            <ShiftTable/>

        </div>
    );
}

export default ProfileContent;