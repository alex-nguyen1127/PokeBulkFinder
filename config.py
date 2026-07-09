""""
eBay API

DB

S3

Flask

Domain constants
"""

import os
from dotenv import load_dotenv

load_dotenv()

# -- eBay API --

EBAY_APP_ID = os.environ.get("EBAY_APP_ID", "")
EBAY_SECRET = os.environ.get("EBAY_SECRET", "")
EBAY_TOKEN_URL = "https://api.ebay.com/identity/v1/oauth2/token"
EBAY_SEARCH_URL = "https://api.ebay.com/buy/browse/v1/item_summary/search"
EBAY_MAX_RESULTS = 50

# -- DB --
#DATABASE_URL controls which databse the app uses

DATABASE_URL = os.environ.get("DATABASE_URL", "")
SQLITE_PATH = os.environ.get("SQLITE_PATH", "data/poke_bulk.db")

# -- AWS S3 --
S3_BUCKET = os.environ.get("S3_BUCKET", "")
S3_PREFIX = os.environ.get("S3_PREFIX", "raw/poke_bulk")
AWS_REGION = os.environ.get("AWS_REGION", "us-east-1")  

# -- Scheduler --
FETCH_INTERVAL_MINUTES = int(os.environ.get("FETCH_INTERVAL_MINUTES", 60))

# -- Flask --
SECRET_KEY = os.environ.get("SECRET_KEY", "dev-secret-change-in-prod")
DEBUG = os.environ.get("FLASK_DEBUG", "true").lower() == "true"
PORT = int(os.environ.get("PORT", 5000))

# -- Lambda --

LAMBDA_BULK_TYPES = os.environ.get(
    "LAMBDA_BULK_TYPES",
    "commons,reverse_holos,holos,pokeballs,masterballs"
).split(",")

LAMBDA_SETS = os.environ.get(
    "LAMBDA_SETS",
    "Any Set,Prismatic Evolutions,Surging Sparks,Pokemon 151"
).split(",")

# -- Domain constants --

BULK_TYPES = {
    "commons": {
        "label":    "Commons",
        "keywords": "common bulk lot",
        "emoji":    "⚪",
    },
    "reverse_holos": {
        "label":    "Reverse Holos",
        "keywords": "reverse holo bulk lot",
        "emoji":    "✨",
    },
    "holos": {
        "label":    "Holos",
        "keywords": "holo rare bulk lot",
        "emoji":    "🌟",
    },
    "pokeballs": {
        "label":    "Poké Balls",
        "keywords": "pokeball stamp bulk lot",
        "emoji":    "🔴",
    },
    "masterballs": {
        "label":    "Master Balls",
        "keywords": "masterball stamp bulk lot",
        "emoji":    "🟣",
    },
}

POKEMON_SETS = [
    "Any Set",
    "Prismatic Evolutions",
    "Surging Sparks",
    "Stellar Crown",
    "Shrouded Fable",
    "Twilight Masquerade",
    "Temporal Forces",
    "Paldean Fates",
    "Paradox Rift",
    "Obsidian Flames",
    "Paldea Evolved",
    "Scarlet & Violet Base",
    "Crown Zenith",
    "Silver Tempest",
    "Lost Origin",
    "Pokemon 151",
    "Fusion Strike",
    "Evolving Skies",
    "Chilling Reign",
    "Battle Styles",
    "Vivid Voltage",
    "Champion's Path",
    "Darkness Ablaze",
    "Rebel Clash",
    "Sword & Shield Base",
]