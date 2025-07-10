import os
from supabase import create_client
from backend.db.models import Filter


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


def add_filter(filter_obj: Filter) -> bool:
    """
    Insert a filter into the filters table.
    Args:
        filter_obj (Filter): The filter object to insert.
    Returns:
        bool: True if insert was successful, False otherwise
    """
    try:
        url = os.environ.get("SUPABASE_URL")
        key = os.environ.get("SUPABASE_KEY")
        supabase = create_client(url, key)

        response = supabase.table('filters').insert(
            {
                "url": filter_obj.url,
                "embedding": filter_obj.embedding.tolist(),
                "relevant": filter_obj.relevant
            }
        ).execute()
        
        return True
    except Exception as e:
        print(f"Error inserting filter: {e}")
        return False

