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
    <ArticleItem v-if="!loading" v-for="article in props.articles" :key="article.id" :article="article" />
    <ArticleItem v-if="loading" v-for="n in nb_loading_elements" :key="n" loading="loading" />
  </div>
</template>
