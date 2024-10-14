

import uvicorn
from fastapi import FastAPI
from .detector import image

app = FastAPI()

app.include_router(image.router)

@app.get("/")
async def alive():
    return {"message": "Projeto PIV Estudo - Modulo Python"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)