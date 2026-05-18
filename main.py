from fastapi import FastAPI
from fastapi.responses import HTMLResponse, FileResponse
import os

app = FastAPI()

# የፋይሎቹ መገኛ (Directory)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# 1. CSS ፋይሉን በቀጥታ ለማቅረብ
@app.get("/style.css")
async def get_css():
    css_path = os.path.join(BASE_DIR, "style.css")
    return FileResponse(css_path, media_type="text/css")

# 2. ዋናውን ድረ-ገጽ (HTML) ለማንበብ
@app.get("/", response_class=HTMLResponse)
async def read_root():
    html_path = os.path.join(BASE_DIR, "index.html")
    with open(html_path, "r", encoding="utf-8") as f:
        return f.read()

# 3. የ LTC አድራሻ ማመንጫ API (ለወደፊቱ የሚሰራ)
@app.post("/api/generate-address")
async def generate_ltc_address():
    return {"status": "success", "address": "LTC_MOCK_ADDRESS_1aB2cD3eF4gH5iJ6"}
