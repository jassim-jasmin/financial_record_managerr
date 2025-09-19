import * as yup from 'yup'

export const transactionSchema = yup.object({
  type: yup.string().oneOf(['expense', 'income', 'transfer']).required(),
  amount: yup.number().positive().required(),
  currency: yup.string().required(),
  description: yup.string(),
  date: yup.date().required(),
  category: yup.string()
})

export const budgetSchema = yup.object({
  name: yup.string().required(),
  amount: yup.number().positive().required(),
  periodType: yup.string().oneOf(['monthly', 'yearly']).required(),
  periodStart: yup.date().required(),
  periodEnd: yup.date().required(),
  categories: yup.object().shape({}),
  rollover: yup.boolean(),
  alertThreshold: yup.number().min(0).max(1).required()
})