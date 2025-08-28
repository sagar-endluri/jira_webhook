from fastapi import FastAPI, Request

app = FastAPI()

@app.post("/")
async def webhook_listener(request: Request):
    body = await request.json()
    print("🔔 Webhook received:", body)
    return {"status": "ok"}