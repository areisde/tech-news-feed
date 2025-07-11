<script setup>
    import ArticleList from '~/components/ArticleList.vue'
    const config = useRuntimeConfig()
    const { data, error } = await useFetch('/api/retrieve')

    console.log("Data fetched:", data)
</script>


<template>
  <header>
    <h1 class="text-3xl font-bold mb-4">Tech News Feed</h1>
    <p class="text-gray-600">Latest articles from various sources</p>
  </header>
  <body>
    
    <ArticleList :articles="data ?? []" />
    <div v-if="error">Error loading articles.</div>
    <div v-else-if="!data">Loading...</div>
  </body>
</template>