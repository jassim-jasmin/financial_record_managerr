import { AppBar as MuiAppBar, Toolbar, Typography, Button } from '@mui/material'
import { useAuth } from '../../hooks/useAuth'

export const AppBar = () => {
  const { signOut } = useAuth()

  return (
    <MuiAppBar position="fixed">
      <Toolbar>
        <Typography variant="h6" component="div" sx={{ flexGrow: 1 }}>
          Financial Manager
        </Typography>
        <Button color="inherit" onClick={signOut}>
          Logout
        </Button>
      </Toolbar>
    </MuiAppBar>
  )
}