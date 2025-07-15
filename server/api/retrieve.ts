export default defineEventHandler(async (event) => {
  const config = useRuntimeConfig()
  const res = await $fetch(`${config.apiBase}/retrieve?code=${config.apiKey}`)
  return res
})