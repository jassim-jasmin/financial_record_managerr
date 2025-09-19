describe('Login Flow', () => {
  it('should login successfully', () => {
    cy.visit('/login')
    cy.get('[data-testid="email"]').type('test@example.com')
    cy.get('[data-testid="password"]').type('password123')
    cy.get('button[type="submit"]').click()
    cy.url().should('include', '/')
  })
})