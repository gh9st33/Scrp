```javascript
import React from 'react';
import { render, screen } from '@testing-library/react';
import Dashboard from '../Dashboard';

test('renders active tasks', () => {
  render(<Dashboard />);
  const activeTasksElement = screen.getByText(/active tasks/i);
  expect(activeTasksElement).toBeInTheDocument();
});

test('renders completed tasks', () => {
  render(<Dashboard />);
  const completedTasksElement = screen.getByText(/completed tasks/i);
  expect(completedTasksElement).toBeInTheDocument();
});

test('renders scraper deployment button', () => {
  render(<Dashboard />);
  const deployButtonElement = screen.getByText(/deploy new scraper/i);
  expect(deployButtonElement).toBeInTheDocument();
});

test('renders data view button', () => {
  render(<Dashboard />);
  const dataViewButtonElement = screen.getByText(/view data/i);
  expect(dataViewButtonElement).toBeInTheDocument();
});

test('renders logs and metrics button', () => {
  render(<Dashboard />);
  const logsMetricsButtonElement = screen.getByText(/view logs and metrics/i);
  expect(logsMetricsButtonElement).toBeInTheDocument();
});
```