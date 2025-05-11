from fastapi import APIRouter, Query
from modules.phase.helpers import specific_volume_liquid, specific_volume_vapor

router = APIRouter()


@router.get("/phase-change-diagram", response_model=dict)
def status(
    pressure: float = Query(None, description="Pressure in MPa"),
):
    print("--------------------------------")
    try:
        print("pressure", pressure)
        liquid_vol = specific_volume_liquid(pressure)
        vapor_vol = specific_volume_vapor(pressure)
        print("liquid_vol", round(liquid_vol, 4))
        print("vapor_vol", round(vapor_vol, 4))
        return {
            "specific_volume_liquid": round(liquid_vol, 4),
            "specific_volume_vapor": round(vapor_vol, 4),
        }
    except Exception as e:
        return {"error": str(e)}
