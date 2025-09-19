import {
  Drawer as MuiDrawer,
  List,
  ListItem,
  ListItemButton,
  ListItemIcon,
  ListItemText,
  Icon
} from '@mui/material'
import { Link } from 'react-router-dom'
import DashboardIcon from '@mui/icons-material/Dashboard'
import { useState } from 'react'

const navItems = [
  { text: 'Dashboard', icon: DashboardIcon, path: '/' },
  { text: 'Transactions', icon: 'receipt', path: '/transactions' },
  { text: 'Budgets', icon: 'account_balance', path: '/budgets' },
  { text: 'Analytics', icon: 'analytics', path: '/analytics' },
  { text: 'Settings', icon: 'settings', path: '/settings' }
]

export const Drawer = () => {
  const [mobileOpen, setMobileOpen] = useState(false)

  const handleDrawerToggle = () => {
    setMobileOpen(!mobileOpen)
  }

  return (
    <>
      {/* Mobile drawer trigger */}
      <MuiDrawer
        variant="temporary"
        open={mobileOpen}
        onClose={handleDrawerToggle}
        ModalProps={{ keepMounted: true }}
      >
        <List>
          {navItems.map((item) => (
            <ListItem key={item.text} disablePadding>
              <ListItemButton component={Link} to={item.path}>
                <ListItemIcon>
                  <Icon>{item.icon}</Icon>
                </ListItemIcon>
                <ListItemText primary={item.text} />
              </ListItemButton>
            </ListItem>
          ))}
        </List>
      </MuiDrawer>
    </>
  )
}