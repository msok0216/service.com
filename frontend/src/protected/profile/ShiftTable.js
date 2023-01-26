import { Table, Button } from 'react-bootstrap';
import { useEffect, useState } from 'react';
function ShiftTable() {
    const [shifts, setShifts] = useState([]);
    const [totalPage, setTotalPage] = useState();
    const [currPage, setCurrPage] = useState(1);

    function fetchShiftData(page) {
        const request = {
            method: 'GET',
            headers: {'Content-Type': 'application/json', 'token': localStorage.getItem('token'), 'page': page}
        };
        fetch('user/shifts', request).then(async response => {
            const data = await response.json();
            if (!response.ok) {
                const error = (data && data.message) || response.statusText;
                return Promise.reject(error);
            }
            console.log(data['shifts'])
            setShifts(data['shifts']);
            setTotalPage(data['pages']);
            setCurrPage(page);
        }).catch(error => {
            console.error('An error occurred', error);
        });
        console.log(page);
    }

    async function increasePage() {
        if (currPage <= totalPage) {
            fetchShiftData(currPage+1);
        }
    }

    function decreasePage() {
        if (currPage > 1) {
            fetchShiftData(currPage-1);  
        }
    }

    useEffect(() => {
        // drawChart(400,600);
        fetchShiftData(1);
        // console.log(shifts);

    }, []);

    return (
        <div className='table-content'>
            <Table className='shift-table'>
                <thead>
                    <tr>
                    {/* <th>#</th> */}
                    <th>Project Name</th>
                    <th>Location</th>
                    <th>Manager</th>
                    <th>Event Time</th>
                    <th>End Time</th>
                    </tr>
                </thead>
                <tbody>
                    {
                        shifts.map(content => <tr key={content.name} className="shifts">
                            {/* <td></td> */}
                            <td className='shift-name'>{content.name}</td>
                            <td className='shift-location'>{content.location}</td>
                            <td className='shift-manager'>{content.manager}</td>
                            <td className='shift-eventTime'>{content.eventTime}</td>
                            <td className='shift-endTime'>{content.endTime}</td>
                        </tr>)
                    }
                </tbody>
            </Table>
            <div className='table-footer'>
                <Button className='page-button' onClick={decreasePage}>Prev</Button>
                <Button className='page-button'>{currPage}</Button>
                <Button className='page-button' onClick={increasePage}>Next</Button>
            </div>
        </div>
    );
}

export default ShiftTable;