```javascript
import React from 'react';
import { render, screen } from '@testing-library/react';
import DataView from '../components/DataView';

test('renders DataView component', () => {
  render(<DataView />);
  const linkElement = screen.getByText(/Data View/i);
  expect(linkElement).toBeInTheDocument();
});

test('fetches data and renders it in the table', async () => {
  const fakeData = [
    { id: '1', name: 'Scraper 1', status: 'Completed', data: 'Data 1' },
    { id: '2', name: 'Scraper 2', status: 'Running', data: 'Data 2' },
  ];
  jest.spyOn(global, 'fetch').mockImplementation(() =>
    Promise.resolve({
      json: () => Promise.resolve(fakeData),
    })
  );

  render(<DataView />);

  const items = await screen.findAllByRole('row');
  expect(items).toHaveLength(3); // header row + 2 data rows

  expect(screen.getByText('Scraper 1')).toBeInTheDocument();
  expect(screen.getByText('Completed')).toBeInTheDocument();
  expect(screen.getByText('Data 1')).toBeInTheDocument();

  expect(screen.getByText('Scraper 2')).toBeInTheDocument();
  expect(screen.getByText('Running')).toBeInTheDocument();
  expect(screen.getByText('Data 2')).toBeInTheDocument();

  global.fetch.mockRestore();
});
```