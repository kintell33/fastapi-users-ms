from main import app

@app.get("/")
async def root():
    return {"status":"ok"}