from fastapi import FastAPI
from modules.systems.router import router as systems_router
from modules.mysc.router import router as mysc_router

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

app.include_router(systems_router, prefix="", tags=["systems"])
app.include_router(mysc_router, prefix="", tags=["mysc"])
