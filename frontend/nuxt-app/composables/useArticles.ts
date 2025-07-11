export const useArticles = () => {
  const config = useRuntimeConfig()
  return useFetch('/retrieve', {
    baseURL: config.public.apiBase,
  })
}