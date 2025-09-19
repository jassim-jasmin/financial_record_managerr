import { defineConfig } from 'cypress'

export default defineConfig({
  e2e: {
    baseUrl: 'http://localhost:5173',  // Vite dev server URL
    setupNodeEvents(on, config) {
      // Implement node event listeners here if needed
    },
  },
  component: {
    devServer: {
      framework: 'react',
      bundler: 'vite',  // Use Vite for faster bundling
    },
    specPattern: 'cypress/component/**/*.cy.{js,jsx,ts,tsx}',
    indexHtmlFile: 'cypress/support/component-index.html',
  },
})