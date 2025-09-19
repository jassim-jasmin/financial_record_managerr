import { useRoutes } from 'react-router-dom'
import { useAuth } from './hooks/useAuth'
import { AppLayout } from './components/common/Layout'
import DashboardPage from './pages/Dashboard/DashboardPage'
import TransactionsPage from './pages/Transactions/TransactionsPage'
import BudgetsPage from './pages/Budgets/BudgetsPage'
import AnalyticsPage from './pages/Analytics/AnalyticsPage'
import SettingsPage from './pages/Settings/SettingsPage'
import LoginPage from './pages/Auth/LoginPage'
import RegisterPage from './pages/Auth/RegisterPage'
import { InstallPrompt } from './components/common/UI/InstallPrompt'

const AppRoutes = () => {
  const { isAuthenticated } = useAuth()
  const routes = isAuthenticated
    ? [
        { path: '/', element: <AppLayout><DashboardPage /></AppLayout> },
        { path: '/transactions', element: <AppLayout><TransactionsPage /></AppLayout> },
        { path: '/budgets', element: <AppLayout><BudgetsPage /></AppLayout> },
        { path: '/analytics', element: <AppLayout><AnalyticsPage /></AppLayout> },
        { path: '/settings', element: <AppLayout><SettingsPage /></AppLayout> }
      ]
    : [
        { path: '/login', element: <LoginPage /> },
        { path: '/register', element: <RegisterPage /> },
        { path: '/', element: <LoginPage /> }
      ]

  return useRoutes(routes)
}

function App() {
  return (
    <>
      <AppRoutes />
      <InstallPrompt />
    </>
  )
}

export default App