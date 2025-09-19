import { useState, useEffect } from 'react'
import { Button, Snackbar } from '@mui/material'

export const InstallPrompt = () => {
  const [deferredPrompt, setDeferredPrompt] = useState<any>(null)
  const [showInstall, setShowInstall] = useState(false)

  useEffect(() => {
    window.addEventListener('beforeinstallprompt', (e) => {
      e.preventDefault()
      setDeferredPrompt(e)
      setShowInstall(true)
    })
  }, [])

  const handleInstall = async () => {
    if (deferredPrompt) {
      deferredPrompt.prompt()
      const { outcome } = await deferredPrompt.userChoice
      if (outcome === 'accepted') {
        setDeferredPrompt(null)
      }
      setShowInstall(false)
    }
  }

  return (
    <Snackbar
      open={showInstall}
      message="Install the app?"
      action={
        <Button color="secondary" size="small" onClick={handleInstall}>
          Install
        </Button>
      }
    />
  )
}