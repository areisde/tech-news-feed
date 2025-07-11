<script setup lang="ts">
    defineProps<{ articles: any[] }>()
</script>


<template>
  <ul>
    <ArticleItem v-for="article in articles" :key="article.id" :article="article" />
  </ul>
</template>

