```javascript
import React, { useState, useEffect } from 'react';
import axios from 'axios';

const DataView = () => {
    const [data, setData] = useState([]);

    useEffect(() => {
        fetchData();
    }, []);

    const fetchData = async () => {
        try {
            const response = await axios.get('/api/data');
            setData(response.data);
        } catch (error) {
            console.error('Error fetching data', error);
        }
    };

    return (
        <div>
            <h2>Data View</h2>
            <table>
                <thead>
                    <tr>
                        <th>Task ID</th>
                        <th>Data</th>
                        <th>Timestamp</th>
                    </tr>
                </thead>
                <tbody>
                    {data.map((item, index) => (
                        <tr key={index}>
                            <td>{item.taskId}</td>
                            <td>{item.data}</td>
                            <td>{item.timestamp}</td>
                        </tr>
                    ))}
                </tbody>
            </table>
        </div>
    );
};

export default DataView;
```