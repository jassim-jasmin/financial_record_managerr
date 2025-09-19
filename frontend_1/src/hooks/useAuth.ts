import { useSelector, useDispatch } from 'react-redux'
import { RootState, AppDispatch } from '../store'
import { setCredentials, logout } from '../store/slices/authSlice'
import { loginUser, logoutUser } from '../services/auth'
import { useEffect } from 'react'

export const useAuth = () => {
  const dispatch = useDispatch<AppDispatch>()
  const { user, token, isAuthenticated } = useSelector((state: RootState) => state.auth)

  useEffect(() => {
    if (token) {
      // Verify token
    }
  }, [token])

  const login = async (credentials: { email: string; password: string }) => {
    try {
      const { access_token, user: userData } = await loginUser(credentials)
      dispatch(setCredentials({ user: userData, token: access_token }))
      return true
    } catch (error) {
      return false
    }
  }

  const register = async (userData: { email: string; password: string; fullName?: string }) => {
    try {
      const { access_token, user: userDataRes } = await registerUser(userData)
      dispatch(setCredentials({ user: userDataRes, token: access_token }))
      return true
    } catch (error) {
      return false
    }
  }

  const signOut = async () => {
    try {
      await logoutUser()
    } catch (error) {
      // Ignore
    }
    dispatch(logout())
  }

  return { user, token, isAuthenticated, login, register, signOut }
}