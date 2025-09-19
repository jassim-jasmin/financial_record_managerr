import { useForm } from 'react-hook-form'
import { yupResolver } from '@hookform/resolvers/yup'
import { loginSchema } from '../../utils/validators'
import { Button, TextField, Box } from '@mui/material'
import { useAuth } from '../../hooks/useAuth'

interface LoginFormData {
  email: string
  password: string
}

export const LoginForm = () => {
  const { login } = useAuth()
  const { register, handleSubmit, formState: { errors } } = useForm<LoginFormData>({
    resolver: yupResolver(loginSchema)
  })

  const onSubmit = async (data: LoginFormData) => {
    await login(data)
  }

  return (
    <Box component="form" onSubmit={handleSubmit(onSubmit)} sx={{ mt: 1 }}>
      <TextField
        margin="normal"
        required
        fullWidth
        id="email"
        label="Email Address"
        autoComplete="email"
        {...register('email')}
        error={!!errors.email}
        helperText={errors.email?.message}
      />
      <TextField
        margin="normal"
        required
        fullWidth
        label="Password"
        type="password"
        id="password"
        autoComplete="current-password"
        {...register('password')}
        error={!!errors.password}
        helperText={errors.password?.message}
      />
      <Button type="submit" fullWidth variant="contained" sx={{ mt: 3 }}>
        Sign In
      </Button>
    </Box>
  )
}