<script setup lang="ts">
    const articles = ref([])
    const filters = ref({})
    const selected_filter = ref("critical")
    const threshold = 0.5 // Point where an article becomes interesting for the category
    const loading = ref(false)

    // Specific news navigator
    const items = ref<TabsItem[]>([
      {
        label: 'Critical Severity',
        value: "critical",
        content: 'Incidents with high severity requiring immediate attention.',
      },
      {
        label: 'Widespread Scope',
        value: "wide",
        content: 'Issues affecting multiple vendors, platforms, or industries.',
      },
      {
        label: 'High User Impact',
        value: "impact",
        content: 'Events with significant end-user disruption or exposure.',
      },
    ])

    const fetch_articles = async () => {
      loading.value = true
      try {
        const response = await $fetch('/api/retrieve')
        console.log('Fetched articles:', response)
        articles.value = Array.isArray(response) ? response : (response.articles || [])
      } catch (err) {
        console.error('Error fetching articles:', err)
        articles.value = []
      }
      loading.value = false
    }

    onMounted(async () => {
      await fetch_articles()
      
      filters.value["latest"] = articles.value;
      filters.value["critical"] = articles.value.filter(article => article.severity_score > threshold);
      filters.value["wide"] = articles.value.filter(article => article.wide_scope_score > threshold);
      filters.value["impact"] = articles.value.filter(article => article.high_impact_score > threshold);
    })



</script>


<template>
  <header class="bg-[rgba(20,31,97,1)]">
    <img src="public/assets/images/nexthink_logo.svg" alt="Nexthink Logo" class="h-20 p-6 inline-block align-middle" />
    <h1 class="text-3xl font-extralight text-white mb-4 inline-block border-l-2 border-white align-middle pl-4 mt-4">Real-Time IT News</h1>

  </header>
  <div class="body-container overflow-hidden relative">
    <div class="menu-background bg-gray-200 w-full h-27 absolute top-0 left-0 z-1 drop-shadow-sm"></div>
    <div class="latest-container bg-gray-200 h-[calc(100vh_-_6rem)] overflow-y-auto scrollbar-hide w-1/2 inline-block">
      <div class="p-5 relative">
        <div class="sticky top-5 z-2">
          <h2 class="text-3xl font-bold inline-block uppercase">Important updates</h2>
          <UButton
            class="cursor-pointer inline-block align-top mt-1 ml-5 *:align-middle *:mx-1"
            icon="i-lucide-refresh-ccw"
            label="Refresh"
            color="neutral"
            size="md"
            @click="fetch_articles"
          />
          <p class="pb-6 pt-2">Fresh updates and breaking incidents across the IT landscape.</p>
        </div>
        <ArticleList :articles="articles" :loading="loading"/>
      </div>
    </div>
    <div class="filters-container border-l-1 border-gray-300 bg-gray-200 h-[calc(100vh_-_6rem)] overflow-y-auto scrollbar-hide w-1/2 inline-block">
      <div class="p-4">
        <UTabs 
          v-model="selected_filter" 
          :items="items" 
          :ui="{ trigger: 'cursor-pointer'}"
          color="neutral" 
          class="w-full pb-6 sticky top-5 z-2" 
        />
        <ArticleList :articles="filters[selected_filter]" :loading="loading" />
      </div>
    </div>
  </div>
</template>

<style>
   .scrollbar-hide::-webkit-scrollbar {
     display: none; /* Chrome, Safari and Opera */
   }
   .scrollbar-hide {
     -ms-overflow-style: none;  /* IE and Edge */
     scrollbar-width: none;  /* Firefox */
   }
</style>