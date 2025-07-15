<script setup lang="ts">
import { ArticleList } from '#components';
    const props = defineProps<{ 
      articles: any[],
      loading : boolean
    }>()

    const nb_loading_elements = 10
</script>


<template>
  <div class="article-container pt-2">
    <div v-if="!loading && articles.length === 0" class="bg-gray-300 p-4">
      <h3 class="text-lg font-bold">No Articles found...</h3>
      <p>Come back later</p>
    </div>
    
    <ArticleItem v-if="!loading" v-for="article in articles" :key="article.id" :article="article" />
    <ArticleItem v-if="loading" v-for="n in nb_loading_elements" :key="n" loading="loading" />
  </div>
</template>
