export const useArticles = () => {
  const config = useRuntimeConfig()
  return useFetch('/api/retrieve', {
    server: false
  })
}