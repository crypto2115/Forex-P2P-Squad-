from fastapi import FastAPI
from fastapi.responses import HTMLResponse, FileResponse
import random
import os

app = FastAPI()

# 1. CSS ፋይሉን በቀጥታ ለማቅረብ (Vercel ላይ በትክክል እንዲሰራ)
@app.get("/style.css")
async def get_css():
    css_path = os.path.join(os.path.dirname(__file__), "style.css")
    return FileResponse(css_path, media_type="text/css")

# 2. ዋናውን ድረ-ገጽ (HTML) ለማንበብ
@app.get("/", response_class=HTMLResponse)
async def read_root():
    html_path = os.path.join(os.path.dirname(__file__), "index.html")
    with open(html_path, "r", encoding="utf-8") as f:
        return f.read()

# 3. የ LTC አድራሻ ማመንጫ API
@app.post("/api/generate-address")
async def generate_ltc_address():
    sample_addresses = [
        "LTC_MOCK_ADDRESS_7xR9wK2pLQzNv5mX",
        "LTC_MOCK_ADDRESS_1aB2cD3eF4gH5iJ6"
    ]
    return {"status": "success", "address": random.choice(sample_addresses)}
