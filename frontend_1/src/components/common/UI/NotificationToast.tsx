import { useSelector } from 'react-redux'
import { Snackbar, Alert } from '@mui/material'
import { RootState } from '../../store'

export const NotificationToast = () => {
  const notifications = useSelector((state: RootState) => state.notifications) // Assume slice

  return (
    <>
      {notifications.map((notif) => (
        <Snackbar
          key={notif.id}
          open={true}
          autoHideDuration={6000}
          onClose={() => {/* handle close */}}
        >
          <Alert severity={notif.type}>{notif.message}</Alert>
        </Snackbar>
      ))}
    </>
  )
}