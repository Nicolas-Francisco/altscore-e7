from fastapi import APIRouter
from fastapi.responses import HTMLResponse
from modules.systems.helpers import get_system_bay, get_random_system
from models.repair.repair_html import REPAIR_HTML

global system
system = get_random_system()

router = APIRouter()


@router.get("/status", response_model=dict)
def status():

    try:
        system_bay = system
        return {"damaged_system": system_bay}
    except Exception as e:
        return {"error": str(e)}


@router.get("/repair-bay", response_model=dict)
def repair():
    try:
        http_response = REPAIR_HTML.format(system_bay=get_system_bay(system))
        return HTMLResponse(content=http_response, media_type="text/html")
    except Exception as e:
        return {"error": str(e)}
