import { io, Socket } from 'socket.io-client'
import { useEffect, useState } from 'react'
import { useSelector } from 'react-redux'
import { RootState } from '../store'

const SOCKET_URL = '/ws'

export const useWebSocket = () => {
  const [socket, setSocket] = useState<Socket | null>(null)
  const token = useSelector((state: RootState) => state.auth.token)

  useEffect(() => {
    if (token) {
      const newSocket = io(SOCKET_URL, {
        auth: { token }
      })
      setSocket(newSocket)

      newSocket.on('connect', () => {
        console.log('WebSocket connected')
      })

      newSocket.on('disconnect', () => {
        console.log('WebSocket disconnected')
      })

      return () => {
        newSocket.close()
      }
    }
  }, [token])

  const sendMessage = (event: string, data: any) => {
    if (socket) {
      socket.emit(event, data)
    }
  }

  return { socket, sendMessage }
}