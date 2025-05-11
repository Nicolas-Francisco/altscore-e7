from fastapi import APIRouter
from fastapi.responses import HTMLResponse

router = APIRouter()


@router.post("/teapot")
def teapot():
    return HTMLResponse(content="I'm a teapot", media_type="text/html", status_code=418)
