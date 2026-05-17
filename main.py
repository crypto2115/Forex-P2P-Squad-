from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
import random

app = FastAPI()

# የ CSS እና የፊት ክፍል ፋይሎችን ለማገናኘት (Static files)
# ማሳሰቢያ፡ index.html ፋይልህን 'templates' በሚል ፎልደር፣ style.css ን ደግሞ 'static' በሚል ፎልደር ውስጥ ማድረግ ትችላለህ
try:
    app.mount("/static", StaticFiles(directory="static"), name="static")
    templates = Jinja2Templates(directory="templates")
except Exception:
    # ፋይሎቹ በአንድ ፎልደር ውስጥ ካሉ ለጊዜው እንዳይዘጋባችሁ የተደረገ ጥንቃቄ
    templates = Jinja2Templates(directory=".")

# የሙከራ ዳታ - ለወደፊቱ ከ Database ጋር የሚገናኝ
withdrawal_rates = {
    "under_10": "160 ETB",
    "above_10": "170 ETB"
}

top_withdrawals = [
    {"rank": 1, "name": "Sen*** Hai***", "phone": "0976***87", "amount": "6,142 ETB", "payments": 18},
    {"rank": 2, "name": "Mua*** Abd***", "phone": "0938***47", "amount": "4,782 ETB", "payments": 3},
    {"rank": 3, "name": "Bam***", "phone": "0951***37", "amount": "3,718 ETB", "payments": 24},
    {"rank": 4, "name": "fil***", "phone": "0936***72", "amount": "3,389 ETB", "payments": 21}
]

# 1. ዋናውን ድረ-ገጽ (UI) ለመክፈት የሚያገለግል Route
@app.get("/")
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# 2. የዋጋ ዝርዝር እና መሪዎችን መረጃ ለፊት ክፍል የሚሰጥ API
@app.get("/api/dashboard")
async def get_dashboard_data():
    return {
        "rates": withdrawal_rates,
        "leaderboard": top_withdrawals
    }

# 3. አዲስ የ LTC Deposit Address ለማመንጨት የሚያገለግል API
@app.post("/api/generate-address")
async def generate_ltc_address():
    # ለሙከራ ያህል በነሲብ የ LTC አድራሻዎችን ያመነጫል
    sample_addresses = [
        "LTC_MOCK_ADDRESS_7xR9wK2pLQzNv5mX",
        "LTC_MOCK_ADDRESS_1aB2cD3eF4gH5iJ6",
        "LTC_MOCK_ADDRESS_9zY8xX7wW6vV5uU4"
    ]
    generated_address = random.choice(sample_addresses)
    return {
        "status": "success",
        "currency": "LTC",
        "address": generated_address
    }
