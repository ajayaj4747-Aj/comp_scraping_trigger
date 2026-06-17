import os, math, re, traceback
from urllib.parse import urlparse
from datetime import datetime

import numpy as np
import pandas as pd
from apify_client import ApifyClient
from deep_translator import GoogleTranslator

# ── Config — overridable via env vars (GitHub Actions sets these) ──
APIFY_TOKEN          = os.environ.get("APIFY_TOKEN", "apify_api_OfHNt7JKFsBMjMWywHCwizhXWztDxU4C2oqs")
ACTOR_ID             = "ZebkvH3nVOrafqr5T"
INPUT_CSV            = os.environ.get("INPUT_CSV", "input_amazon.csv")
OUTPUT_FOLDER        = os.environ.get("OUTPUT_FOLDER", "amazon_output")
INPUT_URL_COLUMN     = "url"
PCODE_COLUMN         = "p_code"
NAME_COLUMN          = "name"
REGION_COLUMN        = "region"
MAX_PAGES_PER_BUCKET = 1
STAR_BUCKETS         = ["one_star", "two_star", "three_star", "four_star", "five_star"]
MAX_REVIEWS_PER_PRODUCT = 500
FORMAT_TYPE          = "current_format"
SORT_BY              = "recent"

os.makedirs(OUTPUT_FOLDER, exist_ok=True)
