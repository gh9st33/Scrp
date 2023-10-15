```javascript
import React from 'react';
import { render, screen } from '@testing-library/react';
import App from '../App';

test('renders learn react link', () => {
  render(<App />);
  const linkElement = screen.getByText(/learn react/i);
  expect(linkElement).toBeInTheDocument();
});

test('renders user authentication component', () => {
  render(<App />);
  const authElement = screen.getByTestId('user-auth');
  expect(authElement).toBeInTheDocument();
});

test('renders dashboard component', () => {
  render(<App />);
  const dashboardElement = screen.getByTestId('dashboard');
  expect(dashboardElement).toBeInTheDocument();
});

test('renders deploy scrapers component', () => {
  render(<App />);
  const deployElement = screen.getByTestId('deploy-scrapers');
  expect(deployElement).toBeInTheDocument();
});

test('renders data view component', () => {
  render(<App />);
  const dataViewElement = screen.getByTestId('data-view');
  expect(dataViewElement).toBeInTheDocument();
});

test('renders logs and metrics component', () => {
  render(<App />);
  const logsMetricsElement = screen.getByTestId('logs-metrics');
  expect(logsMetricsElement).toBeInTheDocument();
});
```