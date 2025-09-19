import { createSlice, PayloadAction } from '@reduxjs/toolkit'
import { Budget } from '../../types/budget'

interface BudgetState {
  budgets: Budget[]
}

const initialState: BudgetState = {
  budgets: []
}

const budgetSlice = createSlice({
  name: 'budget',
  initialState,
  reducers: {
    setBudgets: (state, action: PayloadAction<Budget[]>) => {
      state.budgets = action.payload
    }
  }
})

export const { setBudgets } = budgetSlice.actions
export default budgetSlice.reducer