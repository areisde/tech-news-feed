<script setup lang="ts">
import { ArticleList } from '#components';

    const props = defineProps<{ articles: any[] }>()
</script>


<template>
  <UTimeline
    :items="articles"
    size="xs"
    :ui="{
      date: 'float-end ms-1',
      description: 'px-3 py-2 ring ring-default mt-2 rounded-md text-default'
    }"
    class="w-1/2"
  >
    <template #title="{ item }">
      <h3>{{ item.source }}</h3>
      <h2 class="text-xl">{{ item.title }}</h2>
    </template>

    <template #date="{ item }">
      {{ item.published_at }}
    </template>

    <template #description="{ item }">
      {{ item.body }}
    </template>
  </UTimeline>
</template>
