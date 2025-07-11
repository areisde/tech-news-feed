<script setup lang="ts">
    defineProps<{ article: any }>()
</script>

<template>
  <li>
    <h2>{{ article.title }}</h2>
    <p>{{ article.body }}</p>
    <small>{{ article.published_at }} | {{ article.source }}</small>
  </li>
</template>
