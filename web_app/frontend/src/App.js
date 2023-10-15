```javascript
import React from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import UserAuth from './components/UserAuth';
import Dashboard from './components/Dashboard';
import DeployScrapers from './components/DeployScrapers';
import DataView from './components/DataView';
import LogsMetrics from './components/LogsMetrics';

function App() {
  return (
    <Router>
      <Switch>
        <Route path="/login" component={UserAuth} />
        <Route path="/dashboard" component={Dashboard} />
        <Route path="/deploy" component={DeployScrapers} />
        <Route path="/data" component={DataView} />
        <Route path="/logs" component={LogsMetrics} />
        <Route path="/" component={Dashboard} />
      </Switch>
    </Router>
  );
}

export default App;
```