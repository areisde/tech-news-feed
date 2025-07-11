<script setup lang="ts">
import { ArticleList } from '#components';

    const props = defineProps<{ articles: any[] }>()
</script>


<template>
  <ArticleItem v-for="article in props.articles" :key="article.id" :article="article" />
</template>
