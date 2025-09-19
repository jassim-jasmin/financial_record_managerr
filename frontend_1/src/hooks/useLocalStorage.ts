import { useState, useEffect } from 'react'

export const useLocalStorage = <T>(key: string, initialValue: T) => {
  const [storedValue, setStoredValue] = useState<T>(initialValue)

  useEffect(() => {
    const item = window.localStorage.getItem(key)
    if (item) {
      setStoredValue(JSON.parse(item))
    }
  }, [key])

  const setValue = (value: T) => {
    setStoredValue(value)
    window.localStorage.setItem(key, JSON.stringify(value))
  }

  return { getItem: () => storedValue, setItem: setValue, removeItem: () => window.localStorage.removeItem(key) }
}