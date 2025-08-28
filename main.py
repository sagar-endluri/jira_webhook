from fastapi import FastAPI, Request

app = FastAPI()

@app.post("/")
async def webhook_listener(request: Request):
    try:
        body = await request.json()
    except Exception:
        body = {"error": "No JSON payload"}
    print("🔔 Webhook received:", body)
    return {"status": "ok", "data": body}