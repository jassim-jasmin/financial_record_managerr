# Financial Management Frontend PWA

## Setup

1. Clone repo
2. `npm install`
3. Set .env (VITE_API_URL=http://localhost:8000)
4. `npm run dev`
5. Visit localhost:5173

## Features
- PWA with offline support
- Real-time updates via WebSocket
- Responsive design with MUI
- RTK Query for API integration
- Charts for analytics

## Testing
- Unit: `npm test`
- E2E: `npm run cypress`

## Build
`npm run build`

## PWA
- Installable via browser
- Service worker for caching
- Push notifications ready

## Integration
Assumes backend at /api proxy to localhost:8000