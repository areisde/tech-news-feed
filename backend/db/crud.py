import os
from supabase import create_client


def get_sources():
    """
    Query the 'sources' table and return all sources as a list of dicts.
    Returns:
        List[Dict]: List of sources with keys: id, name, url, type
    """
    sources = []
    
    try:
        url = os.environ.get("SUPABASE_URL")
        key = os.environ.get("SUPABASE_KEY")
        supabase = create_client(url, key)
        response = supabase.table('sources').select('*').execute()
        sources = response.data
    except Exception as e:
        # Log or handle error as needed
        print(f"Error fetching sources: {e}")
        
    return sources