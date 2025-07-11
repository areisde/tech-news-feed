export default defineEventHandler(async (event) => {
  const apiBase = useRuntimeConfig().apiBase
  const res = await $fetch(`${apiBase}/retrieve`)
  return res
})