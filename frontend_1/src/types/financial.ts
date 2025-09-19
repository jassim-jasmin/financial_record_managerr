export enum RecordType {
  EXPENSE = 'expense',
  INCOME = 'income',
  TRANSFER = 'transfer'
}

export interface FinancialRecord {
  id: string
  type: RecordType
  amount: number
  currency: string
  description?: string
  date: Date
  category?: string
  userId: string
  fromUser?: string
  toUser?: string
  customFields: Record<string, any>
  createdAt: Date
  updatedAt: Date
}