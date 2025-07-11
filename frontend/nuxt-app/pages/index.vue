<script setup>
    import ArticleList from '~/components/ArticleList.vue'
    const config = useRuntimeConfig()
    const { data, error } = await useFetch('/api/retrieve')

    console.log("Data fetched:", data)
</script>


<template>
  <div>
    <h1>Tech News Feed</h1>
    <ArticleList :articles="data ?? []" />
    <div v-if="error">Error loading articles.</div>
    <div v-else-if="!data">Loading...</div>
  </div>
</template>