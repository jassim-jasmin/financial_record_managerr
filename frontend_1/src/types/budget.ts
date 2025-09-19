export enum PeriodType {
  MONTHLY = 'monthly',
  YEARLY = 'yearly'
}

export interface Budget {
  id: string
  name: string
  amount: number
  currency: string
  periodType: PeriodType
  periodStart: Date
  periodEnd: Date
  categories: Record<string, number>
  userId: string
  rollover: boolean
  alertThreshold: number
  createdAt: Date
  updatedAt: Date
}

export interface BudgetProgress {
  budgetId: string
  spent: number
  remaining: number
  percentage: number
}