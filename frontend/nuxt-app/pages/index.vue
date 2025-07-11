<script setup lang="ts">
    import { useArticles } from '~/composables/useArticles'

    const { data: articles } = useArticles()
</script>


<template>
  <div>
    <h1>Welcome to Tech News Feed</h1>
    <p>This is your home page.</p>
    <ArticleList :articles="data ?? []" />
  </div>
</template>

