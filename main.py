from fastapi import FastAPI, Request

app = FastAPI()

@app.get("/")
async def home():
    return {"message": "FastAPI webhook listener is running 🚀"}

@app.post("/")
async def webhook_listener(request: Request):
    # Get the raw payload (bytes)
    payload_bytes = await request.body()
    # Decode to string for printing (assumes utf-8, which is typical for webhooks)
    payload_str = payload_bytes.decode('utf-8', errors='replace')
    print("🔔 Raw payload received:", payload_str)
    return {"status": "ok", "received": bool(payload_str)}