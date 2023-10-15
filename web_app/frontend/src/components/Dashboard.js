```javascript
import React, { Component } from 'react';
import axios from 'axios';

class Dashboard extends Component {
  constructor(props) {
    super(props);
    this.state = {
      tasks: [],
      isLoading: true,
      error: null,
    };
  }

  componentDidMount() {
    this.fetchTasks();
  }

  fetchTasks() {
    axios.get('/api/tasks')
      .then(response => {
        this.setState({
          tasks: response.data,
          isLoading: false,
        });
      })
      .catch(error => this.setState({ error, isLoading: false }));
  }

  render() {
    const { isLoading, tasks, error } = this.state;
    return (
      <React.Fragment>
        <h1>Dashboard</h1>
        {error ? <p>{error.message}</p> : null}
        {!isLoading ? (
          tasks.map(task => {
            const { _id, name, status } = task;
            return (
              <div key={_id}>
                <p>Name: {name}</p>
                <p>Status: {status}</p>
              </div>
            );
          })
        ) : (
          <h3>Loading...</h3>
        )}
      </React.Fragment>
    );
  }
}

export default Dashboard;
```