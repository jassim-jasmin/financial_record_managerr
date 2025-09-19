import { Grid, Card, CardContent, Typography } from '@mui/material'
import { PieChart } from '../../components/common/Charts/PieChart'
import { LineChart } from '../../components/common/Charts/LineChart'
import { useGetAnalyticsQuery } from '../../store/api/recordsApi'
import { formatCurrency } from '../../utils/formatters'

export default function DashboardPage() {
  const { data: analytics } = useGetAnalyticsQuery()

  return (
    <Grid container spacing={3}>
      <Grid item xs={12} sm={6} md={3}>
        <Card>
          <CardContent>
            <Typography color="textSecondary" gutterBottom>
              Total Income
            </Typography>
            <Typography variant="h5" component="div">
              {formatCurrency(analytics?.totalIncome || 0)}
            </Typography>
          </CardContent>
        </Card>
      </Grid>
      {/* More cards */}
      <Grid item xs={12} md={6}>
        <PieChart />
      </Grid>
      <Grid item xs={12} md={6}>
        <LineChart />
      </Grid>
    </Grid>
  )
}