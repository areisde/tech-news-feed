<script setup>
import { ar } from '@nuxt/ui/runtime/locale/index.js'

    const articles = ref([])

    const fetch_articles = async () => {
      try {
        const response = await $fetch('/api/retrieve')
        console.log('Fetched articles:', response)
        articles.value = Array.isArray(response) ? response : (response.articles || [])
      } catch (err) {
        console.error('Error fetching articles:', err)
        articles.value = []
      }
    }

    onMounted(async () => {
      await fetch_articles()
      console.log('Articles on mount:', articles.value)
    })

</script>


<template>
  <header class="bg-[rgba(20,31,97,1)]">
    <img src="public/assets/images/nexthink_logo.svg" alt="Nexthink Logo" class="h-20 p-6 inline-block align-middle" />
    <h1 class="text-3xl font-extralight text-white mb-4 inline-block border-l-2 border-white align-middle pl-4 mt-4">IT Latest</h1>
    <UButton
      class="cursor-pointer float-end mt-5 me-6"
      icon="i-lucide-refresh-ccw"
      label="Refresh"
      color="neutral"
      size="xl"
      @click="fetch_articles"
    />

  </header>
  <body class="bg-gray-200 h-[calc(100vh_-_5rem)] overflow-y-auto w-1/2">
    <div class="p-4">
      <ArticleList :articles="articles" />
    </div>
  </body>
</template>