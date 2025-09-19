import { format } from 'date-fns'

export const formatCurrency = (amount: number, currency: string = 'USD') => {
  return new Intl.NumberFormat('en-US', {
    style: 'currency',
    currency
  }).format(amount)
}

export const formatDate = (date: Date) => {
  return format(date, 'MMM dd, yyyy')
}