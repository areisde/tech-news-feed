export default defineEventHandler(async (event) => {
  const config = useRuntimeConfig()
  console.log(config.apiKey)
  console.log(config.apiBase)
  const res = await $fetch(`${config.apiBase}/retrieve?code=${config.apiKey}`)
  return res
})