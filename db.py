from dotenv import load_dotenv
load_dotenv()

import os
from supabase import create_client

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")


supabase = create_client(SUPABASE_URL, SUPABASE_KEY)


def add_fish(user_id: int, amount: int = 1):
    # получить текущую рыбу
    res = (
        supabase
        .table("users")
        .select("fish")
        .eq("user_id", user_id)
        .execute()
    )

    if res.data:
        fish = res.data[0]["fish"] + amount
    else:
        fish = amount

    # сохранить в БД
    (
        supabase
        .table("users")
        .upsert({
            "user_id": user_id,
            "fish": fish
        })
        .execute()
    )

    return fish
print("URL:", SUPABASE_URL)
print("KEY:", "OK" if SUPABASE_KEY else "NO")

