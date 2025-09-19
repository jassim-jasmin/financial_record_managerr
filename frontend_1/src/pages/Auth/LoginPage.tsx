import { Container, Paper } from '@mui/material'
import { LoginForm } from '../../components/auth/LoginForm'

export default function LoginPage() {
  return (
    <Container component="main" maxWidth="xs">
      <Paper sx={{ mt: 8, p: 4 }}>
        <LoginForm />
      </Paper>
    </Container>
  )
}