import { createApi, fetchBaseQuery } from '@reduxjs/toolkit/query/react'
import type { RootState } from '../index'
import { Budget, BudgetProgress } from '../../types/budget'

const baseQuery = fetchBaseQuery({
  baseUrl: '/api/budgets/',
  prepareHeaders: (headers, { getState }) => {
    const token = (getState() as RootState).auth.token
    if (token) {
      headers.set('authorization', `Bearer ${token}`)
    }
    return headers
  }
})

export const budgetsApi = createApi({
  reducerPath: 'budgetsApi',
  baseQuery,
  tagTypes: ['Budget'],
  endpoints: (builder) => ({
    getBudgets: builder.query<Budget[], void>({
      query: () => '',
      providesTags: ['Budget']
    }),
    createBudget: builder.mutation<Budget, Partial<Budget>>({
      query: (budget) => ({
        url: '',
        method: 'POST',
        body: budget
      }),
      invalidatesTags: ['Budget']
    }),
    updateBudget: builder.mutation<Budget, { id: string; budget: Partial<Budget> }>({
      query: ({ id, budget }) => ({
        url: `${id}`,
        method: 'PUT',
        body: budget
      }),
      invalidatesTags: ['Budget']
    }),
    deleteBudget: builder.mutation<void, string>({
      query: (id) => ({
        url: `${id}`,
        method: 'DELETE'
      }),
      invalidatesTags: ['Budget']
    }),
    getBudgetProgress: builder.query<BudgetProgress, string>({
      query: (id) => `${id}/progress`
    })
  })
})

export const { useGetBudgetsQuery, useCreateBudgetMutation, useUpdateBudgetMutation, useDeleteBudgetMutation, useGetBudgetProgressQuery } = budgetsApi