```javascript
import React from 'react';
import { render, fireEvent } from '@testing-library/react';
import DeployScrapers from '../components/DeployScrapers';

test('renders deploy scrapers component', () => {
  const { getByText } = render(<DeployScrapers />);
  const linkElement = getByText(/Deploy a new scraper/i);
  expect(linkElement).toBeInTheDocument();
});

test('handles form submission', () => {
  const mockSubmit = jest.fn();
  const { getByLabelText, getByText } = render(<DeployScrapers onSubmit={mockSubmit} />);
  
  const scraperNameInput = getByLabelText(/Scraper Name/i);
  const scraperUrlInput = getByLabelText(/Scraper URL/i);
  const submitButton = getByText(/Deploy/i);

  fireEvent.change(scraperNameInput, { target: { value: 'Test Scraper' } });
  fireEvent.change(scraperUrlInput, { target: { value: 'http://testscraper.com' } });
  fireEvent.click(submitButton);

  expect(mockSubmit).toHaveBeenCalled();
  expect(mockSubmit).toHaveBeenCalledWith({
    scraperName: 'Test Scraper',
    scraperUrl: 'http://testscraper.com',
  });
});
```