from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, FileResponse
import random

app = FastAPI()

# የሙከራ ዳታ
withdrawal_rates = {"under_10": "160 ETB", "above_10": "170 ETB"}
top_withdrawals = [
    {"rank": 1, "name": "Sen*** Hai***", "phone": "0976***87", "amount": "6,142 ETB", "payments": 18},
    {"rank": 2, "name": "Mua*** Abd***", "phone": "0938***47", "amount": "4,782 ETB", "payments": 3},
    {"rank": 3, "name": "Bam***", "phone": "0951***37", "amount": "3,718 ETB", "payments": 24},
    {"rank": 4, "name": "fil***", "phone": "0936***72", "amount": "3,389 ETB", "payments": 21}
]

# 1. CSS ፋይሉን በቀጥታ ለማቅረብ
@app.get("/style.css")
async def get_css():
    return FileResponse("style.css", media_type="text/css")

# 2. ዋናውን ድረ-ገጽ (HTML) ለማንበብ
@app.get("/", response_class=HTMLResponse)
async def read_root():
    with open("index.html", "r", encoding="utf-8") as f:
        return f.read()

# 3. የ LTC አድራሻ ማመንጫ API
@app.post("/api/generate-address")
async def generate_ltc_address():
    sample_addresses = [
        "LTC_MOCK_ADDRESS_7xR9wK2pLQzNv5mX",
        "LTC_MOCK_ADDRESS_1aB2cD3eF4gH5iJ6"
    ]
    return {"status": "success", "address": random.choice(sample_addresses)}
