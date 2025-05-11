from fastapi import FastAPI
from modules.systems.router import router as systems_router
from modules.mysc.router import router as mysc_router
from modules.phase.router import router as phase_router
app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

app.include_router(systems_router, prefix="", tags=["systems"])
app.include_router(mysc_router, prefix="", tags=["mysc"])
app.include_router(phase_router, prefix="", tags=["phase-change"])
