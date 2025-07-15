// server/api/sources/get.ts

import { createClient } from '@supabase/supabase-js'

export default defineEventHandler(async () => {
  const supabaseUrl = process.env.SUPABASE_URL || ''
  const supabaseKey = process.env.SUPABASE_KEY || ''
  const supabase = createClient(supabaseUrl, supabaseKey)

  const { data, error } = await supabase.from('sources').select('*')

  if (error) {
    console.error('Error fetching sources:', error)
    throw createError({ statusCode: 500, message: 'Failed to fetch sources' })
  }

  return data
})