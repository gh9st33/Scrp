```javascript
import React from 'react';
import { render, fireEvent } from '@testing-library/react';
import UserAuth from '../components/UserAuth';

test('renders login form', () => {
  const { getByLabelText } = render(<UserAuth />);
  const usernameElement = getByLabelText(/username/i);
  const passwordElement = getByLabelText(/password/i);
  expect(usernameElement).toBeInTheDocument();
  expect(passwordElement).toBeInTheDocument();
});

test('submits form with user input', () => {
  const mockLogin = jest.fn();
  const { getByLabelText, getByText } = render(<UserAuth login={mockLogin} />);
  const usernameElement = getByLabelText(/username/i);
  const passwordElement = getByLabelText(/password/i);
  const submitButton = getByText(/submit/i);

  fireEvent.change(usernameElement, { target: { value: 'testuser' } });
  fireEvent.change(passwordElement, { target: { value: 'testpass' } });
  fireEvent.click(submitButton);

  expect(mockLogin).toHaveBeenCalledWith('testuser', 'testpass');
});
```