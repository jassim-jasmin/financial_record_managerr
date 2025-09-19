export interface User {
  id: string
  email: string
  fullName?: string
  isActive: boolean
  isAdmin: boolean
}

export interface Token {
  access_token: string
  refresh_token: string
  token_type: 'bearer'
}