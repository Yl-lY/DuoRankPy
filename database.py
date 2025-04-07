import os
from dotenv import load_dotenv
from supabase import create_client, Client

load_dotenv()

url: str = os.getenv("SUPABASE_URL")
key: str = os.getenv("SUPABASE_KEY")
supabase: Client = create_client(url, key)

def get_competitors():
    response = supabase.table("Competitors").select("*").execute()
    return response

def get_competitor(user):
    response = supabase.table("Competitors").select("*").eq("name", user).execute()
    return response

def post_competitor(user):
    response = supabase.table("Competitors").insert(user).execute()
    return response

def update_competitor(user):
    response = supabase.table("Competitors").update(user).eq("name", user['name']).execute()
    return response

