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
      <span>{{ item.source }}</span>
      <span class="float-end">{{ item.title }}</span>
    </template>

    <template #date="{ item }">
      {{ item.published_at }}
    </template>

    <template #description="{ item }">
      {{ item.body }}
    </template>
  </UTimeline>
</template>
