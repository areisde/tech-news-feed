// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  compatibilityDate: '2025-05-15',
  devtools: { enabled: true },
  modules: [
    '@nuxt/ui'
  ],
  css: ['~/assets/css/main.css'],
  runtimeConfig: {
    apiBase: "https://tech-news-light-e8dvcca4ajgpdpha.westeurope-01.azurewebsites.net/api",
    apiKey: process.env.BACKEND_API_KEY
  }
})
