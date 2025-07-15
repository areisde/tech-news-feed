<script setup lang="ts">

    const articles = ref([])
    const sources = ref([])
    const selected_filter = ref("critical")
    const threshold = 0.5 // Point where an article becomes interesting for the category
    const loading = ref(false)
    const selectedSources = ref<Record<string, boolean>>({})

    const normalizeSourceKey = (name: string) => {
      if (!name) return ''

      const cleaned = name.toLowerCase().replace(/[^a-z0-9]/g, '') // remove spaces, dashes, etc.

      // Special case correction
      if (cleaned === 'computersweekly') return 'computerweekly'

      return cleaned
    }

    const isSourceSelected = (article: any): boolean => {
      const sourceKey = normalizeSourceKey(article.source)
      return selectedSources.value[sourceKey] !== false
    }

    const filteredArticles = computed(() => {
      const sourceFiltered = articles.value.filter(isSourceSelected)

      return {
        latest: sourceFiltered,
        critical: sourceFiltered.filter(a => a.severity_score > threshold),
        wide: sourceFiltered.filter(a => a.wide_scope_score > threshold),
        impact: sourceFiltered.filter(a => a.high_impact_score > threshold),
      }
    })

    const sourceItems = computed(() =>
      sources.value.map(source => {
        const key = normalizeSourceKey(source.name)
        return {
          label: source.name,
          icon: source.type === "rss" ? 'i-lucide-rss' : 'i-lucide-link',
          type: 'checkbox' as const,
          checked: selectedSources.value[key],
          onUpdateChecked(checked: boolean) {
            selectedSources.value[key] = checked
          }
        }
      })
    )

    // Specific news navigator
    const tabItems = ref<TabsItem[]>([
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
        articles.value = Array.isArray(response) ? response : (response.articles || [])
      } catch (err) {
        console.error('Error fetching articles:', err)
        articles.value = []
      }
      loading.value = false
    }

    const fetch_sources = async () => {
      try {
        const response = await $fetch('/api/sources/get')
        const data = Array.isArray(response) ? response : (response.sources || [])
        sources.value = data

        // Initialize selectedSources map with all sources set to true (or false if you prefer)
        data.forEach((source: { id: string; name: string }) => {
          const key = normalizeSourceKey(source.name)
          selectedSources.value[key] = true
        })
      } catch (err) {
        console.error('Error fetching sources:', err)
        sources.value = []
      }
    }

    onMounted(async () => {
      await Promise.all([fetch_articles(), fetch_sources()]) // Parallel loading
    })



</script>


<template>
  <header class="bg-[rgba(20,31,97,1)]">
    <img src="public/assets/images/nexthink_logo.svg" alt="Nexthink Logo" class="h-20 p-6 inline-block align-middle" />
    <h1 class="text-3xl font-extralight text-white mb-4 inline-block border-l-2 border-white align-middle pl-4 mt-4">Real-Time IT News</h1>
    <div class="sources-buttons float-end mt-6 mr-4">
      <UDropdownMenu :items="sourceItems">
        <UButton label="Sources" color="neutral" icon="i-lucide-library"/>
      </UDropdownMenu>
    </div>
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
            :loading="loading"
            @click="fetch_articles"
          />
          <p class="pb-6 pt-2">Fresh updates and breaking incidents across the IT landscape.</p>
        </div>
        <ArticleList :articles="filteredArticles.latest" :loading="loading" />
      </div>
    </div>
    <div class="filters-container border-l-1 border-gray-300 bg-gray-200 h-[calc(100vh_-_6rem)] overflow-y-auto scrollbar-hide w-1/2 inline-block">
      <div class="p-4">
        <UTabs 
          v-model="selected_filter" 
          :items="tabItems" 
          :ui="{ trigger: 'cursor-pointer'}"
          color="neutral" 
          class="w-full pb-6 sticky top-5 z-2" 
        />
        <ArticleList :articles="filteredArticles[selected_filter]" :loading="loading" />
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