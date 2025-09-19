import { Box, Container } from '@mui/material'
import { AppBar } from '../Navigation/AppBar'
import { Drawer } from '../Navigation/Drawer'

export const AppLayout = ({ children }: { children: React.ReactNode }) => {
  return (
    <Box sx={{ display: 'flex' }}>
      <AppBar />
      <Drawer />
      <Box component="main" sx={{ flexGrow: 1, p: 3 }}>
        <Container maxWidth="lg">
          {children}
        </Container>
      </Box>
    </Box>
  )
}