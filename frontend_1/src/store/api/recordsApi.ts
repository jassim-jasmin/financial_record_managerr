import { createApi, fetchBaseQuery } from '@reduxjs/toolkit/query/react'
import type { RootState } from '../index'
import { FinancialRecord, RecordType } from '../../types/financial'

const baseQuery = fetchBaseQuery({
  baseUrl: '/api/records/',
  prepareHeaders: (headers, { getState }) => {
    const token = (getState() as RootState).auth.token
    if (token) {
      headers.set('authorization', `Bearer ${token}`)
    }
    return headers
  }
})

export const recordsApi = createApi({
  reducerPath: 'recordsApi',
  baseQuery,
  tagTypes: ['Record'],
  endpoints: (builder) => ({
    getRecords: builder.query<FinancialRecord[], { type?: RecordType; category?: string }>({
      query: (params) => ({ url: '', params }),
      providesTags: ['Record']
    }),
    createRecord: builder.mutation<FinancialRecord, Partial<FinancialRecord>>({
      query: (record) => ({
        url: '',
        method: 'POST',
        body: record
      }),
      invalidatesTags: ['Record']
    }),
    updateRecord: builder.mutation<FinancialRecord, { id: string; record: Partial<FinancialRecord> }>({
      query: ({ id, record }) => ({
        url: `${id}`,
        method: 'PUT',
        body: record
      }),
      invalidatesTags: ['Record']
    }),
    deleteRecord: builder.mutation<void, string>({
      query: (id) => ({
        url: `${id}`,
        method: 'DELETE'
      }),
      invalidatesTags: ['Record']
    }),
    getAnalytics: builder.query<{ totalIncome: number; totalExpense: number; net: number }, void>({
      query: () => 'analytics'
    })
  })
})

export const { useGetRecordsQuery, useCreateRecordMutation, useUpdateRecordMutation, useDeleteRecordMutation, useGetAnalyticsQuery } = recordsApi