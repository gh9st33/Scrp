```javascript
import React from 'react';
import { render, screen } from '@testing-library/react';
import LogsMetrics from '../components/LogsMetrics';

test('renders LogsMetrics component', () => {
  render(<LogsMetrics />);
  const linkElement = screen.getByText(/Logs and Metrics/i);
  expect(linkElement).toBeInTheDocument();
});

test('displays logs and metrics data', async () => {
  render(<LogsMetrics />);
  
  // Assuming that the LogsMetrics component fetches data and displays it in an element with the id 'logs-metrics-data'
  const dataElement = await screen.findByTestId('logs-metrics-data');
  
  // Check that the data element is in the document and is not empty
  expect(dataElement).toBeInTheDocument();
  expect(dataElement.textContent).not.toBe('');
});
```