import { CircularProgress } from '@mui/material'
import { Doughnut } from 'react-chartjs-2'
import { useGetBudgetProgressQuery } from '../../store/api/budgetsApi'
import { Chart as ChartJS, ArcElement, Tooltip, Legend } from 'chart.js'

ChartJS.register(ArcElement, Tooltip, Legend)

export const BudgetProgress = ({ budgetId }: { budgetId: string }) => {
  const { data: progress, isLoading } = useGetBudgetProgressQuery(budgetId)

  if (isLoading) return <CircularProgress />

  const data = {
    labels: ['Spent', 'Remaining'],
    datasets: [
      {
        data: [progress?.spent, progress?.remaining],
        backgroundColor: ['#FF6384', '#36A2EB']
      }
    ]
  }

  return <Doughnut data={data} />
}