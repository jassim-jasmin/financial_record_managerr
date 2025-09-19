import { configureStore } from '@reduxjs/toolkit'
import { setupListeners } from '@reduxjs/toolkit/query'
import { authApi } from './api/authApi'
import { recordsApi } from './api/recordsApi'
import { budgetsApi } from './api/budgetsApi'
import authSlice from './slices/authSlice'
import financialSlice from './slices/financialSlice'
import budgetSlice from './slices/budgetSlice'

export const store = configureStore({
  reducer: {
    [authApi.reducerPath]: authApi.reducer,
    [recordsApi.reducerPath]: recordsApi.reducer,
    [budgetsApi.reducerPath]: budgetsApi.reducer,
    auth: authSlice,
    financial: financialSlice,
    budget: budgetSlice
  },
  middleware: (getDefaultMiddleware) =>
    getDefaultMiddleware().concat(
      authApi.middleware,
      recordsApi.middleware,
      budgetsApi.middleware
    )
})

setupListeners(store.dispatch)

export type RootState = ReturnType<typeof store.getState>
export type AppDispatch = typeof store.dispatch