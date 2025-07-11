<script setup lang="ts">
    defineProps<{ article: any }>()
</script>

<template>
  <div class="mb-5 border-b-1 border-gray-300 pb-4">
    <h2 class="text-xl font-bold">{{ article.title }}</h2>
    <p class="text-justify">{{ article.body }}</p>
    <p><small>{{ article.published_at }} | {{ article.source }}</small></p>
  </div>
</template>
