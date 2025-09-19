import api from './api'
import { User } from '../types/auth'

export const loginUser = async (credentials: { email: string; password: string }) => {
  const response = await api.post('/auth/login', credentials)
  return response.data
}

export const registerUser = async (userData: { email: string; password: string; fullName?: string }) => {
  const response = await api.post('/auth/register', userData)
  return response.data
}

export const logoutUser = async () => {
  await api.post('/auth/logout')
}