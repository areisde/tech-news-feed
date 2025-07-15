<script setup lang="ts">
    defineProps<{ 
      article: any,
      loading: boolean
    }>()
</script>

<template>
  <div class="mb-5 border-b-1 border-gray-300 pb-4">
    <h2 class="text-xl font-bold">{{ !loading ? article.title : '' }} <USkeleton v-if="loading" class="h-6 w-[200px] mb-3" /></h2>
    <p class="text-justify line-clamp-3">{{ !loading ? article.body : '' }} <USkeleton v-if="loading" class="h-15 mb-1 w-[100%]" /></p>
    <p class="mt-2"><small>{{ !loading ? article.published_at : ''}} <USkeleton v-if="loading" class="h-2 w-[100px] inline-block" /> | {{ !loading ? article.source : ''}} <USkeleton v-if="loading" class="h-2 w-[100px] inline-block" /></small></p>
  </div>
</template>
