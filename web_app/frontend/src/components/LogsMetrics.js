```javascript
import React, { useState, useEffect } from 'react';
import axios from 'axios';

const LogsMetrics = () => {
    const [logs, setLogs] = useState([]);
    const [metrics, setMetrics] = useState([]);

    useEffect(() => {
        fetchLogs();
        fetchMetrics();
    }, []);

    const fetchLogs = async () => {
        const response = await axios.get('/api/logs');
        setLogs(response.data);
    };

    const fetchMetrics = async () => {
        const response = await axios.get('/api/metrics');
        setMetrics(response.data);
    };

    return (
        <div>
            <h2>Logs</h2>
            <ul>
                {logs.map((log, index) => (
                    <li key={index}>{log}</li>
                ))}
            </ul>
            <h2>Metrics</h2>
            <ul>
                {metrics.map((metric, index) => (
                    <li key={index}>{metric}</li>
                ))}
            </ul>
        </div>
    );
};

export default LogsMetrics;
```