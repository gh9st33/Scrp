```javascript
import React, { useState } from 'react';
import axios from 'axios';

const UserAuth = () => {
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');
    const [error, setError] = useState('');

    const handleLogin = async (e) => {
        e.preventDefault();
        try {
            const response = await axios.post('/api/login', { username, password });
            localStorage.setItem('token', response.data.token);
        } catch (err) {
            setError('Invalid username or password');
        }
    };

    return (
        <div>
            <form onSubmit={handleLogin}>
                <label>
                    Username:
                    <input type="text" value={username} onChange={e => setUsername(e.target.value)} />
                </label>
                <label>
                    Password:
                    <input type="password" value={password} onChange={e => setPassword(e.target.value)} />
                </label>
                <input type="submit" value="Login" />
            </form>
            {error && <p>{error}</p>}
        </div>
    );
};

export default UserAuth;
```