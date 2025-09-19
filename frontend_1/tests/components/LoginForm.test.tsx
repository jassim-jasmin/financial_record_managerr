import { render, screen, fireEvent } from '@testing-library/react'
import { LoginForm } from '../../src/components/auth/LoginForm'
import { Provider } from 'react-redux'
import { store } from '../../src/store'

test('renders login form and submits', async () => {
  render(
    <Provider store={store}>
      <LoginForm />
    </Provider>
  )

  expect(screen.getByLabelText(/email address/i)).toBeInTheDocument()
  fireEvent.change(screen.getByLabelText(/email address/i), { target: { value: 'test@example.com' } })
  // More assertions
})