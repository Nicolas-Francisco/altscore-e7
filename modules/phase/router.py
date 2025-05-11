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
        print("liquid_vol", liquid_vol)
        print("vapor_vol", vapor_vol)
        return {
            "specific_volume_liquid": liquid_vol,
            "specific_volume_vapor": vapor_vol,
        }
    except Exception as e:
        return {"error": str(e)}
