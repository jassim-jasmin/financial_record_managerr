import { useLocalStorage } from '../hooks/useLocalStorage'

export const useSecureStorage = () => {
  const { getItem, setItem, removeItem } = useLocalStorage()

  const setSecureItem = (key: string, value: string) => {
    // Simple encryption (use proper crypto in prod)
    const encrypted = btoa(value)
    setItem(key, encrypted)
  }

  const getSecureItem = (key: string) => {
    const encrypted = getItem(key)
    return encrypted ? atob(encrypted) : null
  }

  return { setSecureItem, getSecureItem, removeItem }
}