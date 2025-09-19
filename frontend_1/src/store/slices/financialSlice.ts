import { createSlice, PayloadAction } from '@reduxjs/toolkit'
import { FinancialRecord } from '../../types/financial'

interface FinancialState {
  records: FinancialRecord[]
  filters: { type?: string; category?: string }
}

const initialState: FinancialState = {
  records: [],
  filters: {}
}

const financialSlice = createSlice({
  name: 'financial',
  initialState,
  reducers: {
    setRecords: (state, action: PayloadAction<FinancialRecord[]>) => {
      state.records = action.payload
    },
    setFilters: (state, action: PayloadAction<FinancialState['filters']>) => {
      state.filters = action.payload
    }
  }
})

export const { setRecords, setFilters } = financialSlice.actions
export default financialSlice.reducer