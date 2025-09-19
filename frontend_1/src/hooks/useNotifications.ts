import { useEffect } from 'react'
import { useWebSocket } from './useWebSocket'
import { useDispatch } from 'react-redux'
import { addNotification } from '../store/slices/notificationSlice' // Assume slice

export const useNotifications = () => {
  const { socket } = useWebSocket()
  const dispatch = useDispatch()

  useEffect(() => {
    if (socket) {
      socket.on('notification', (data) => {
        dispatch(addNotification(data))
      })
    }
  }, [socket, dispatch])
}