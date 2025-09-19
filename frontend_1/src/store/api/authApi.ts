import { createApi, fetchBaseQuery } from '@reduxjs/toolkit/query/react'
import { RootState } from '../index'
import { loginUser, registerUser, logoutUser } from '../../services/auth'

const baseQuery = fetchBaseQuery({
  baseUrl: '/api/auth/',
  prepareHeaders: (headers, { getState }) => {
    const token = (getState() as RootState).auth.token
    if (token) {
      headers.set('authorization', `Bearer ${token}`)
    }
    return headers
  }
})

export const authApi = createApi({
  reducerPath: 'authApi',
  baseQuery,
  endpoints: (builder) => ({
    login: builder.mutation({
      query: ({ email, password }) => ({
        url: 'login',
        method: 'POST',
        body: { email, password }
      }),
      async onQueryStarted(arg, { dispatch, queryFulfilled }) {
        try {
          const { data } = await queryFulfilled
          dispatch(loginUser(data))
        } catch (error) {
          // Handle error
        }
      }
    }),
    register: builder.mutation({
      query: (user) => ({
        url: 'register',
        method: 'POST',
        body: user
      })
    }),
    logout: builder.mutation({
      query: () => ({
        url: 'logout',
        method: 'POST'
      }),
      async onQueryStarted(_, { dispatch, queryFulfilled }) {
        try {
          await queryFulfilled
          dispatch(logoutUser())
        } catch (error) {
          // Handle error
        }
      }
    })
  })
})

export const { useLoginMutation, useRegisterMutation, useLogoutMutation } = authApi