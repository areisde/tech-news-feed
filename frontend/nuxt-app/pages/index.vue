<script setup>
    import ArticleList from '~/components/ArticleList.vue'
    const config = useRuntimeConfig()
    const { data, error } = await useFetch('/api/retrieve')

    console.log("Data fetched:", data)
</script>


<template>
  <header class="bg-[rgba(20,31,97,1)]">
    <img src="public/assets/images/nexthink_logo.svg" alt="Nexthink Logo" class="h-20 p-6 inline-block align-middle" />
    <h1 class="text-3xl font-extralight text-white mb-4 inline-block border-l-2 border-white align-middle pl-4 mt-4">IT Latest</h1>
  </header>
  <body>
    
    <ArticleList :articles="data ?? []" />
    <div v-if="error">Error loading articles.</div>
    <div v-else-if="!data">Loading...</div>
  </body>
</template>