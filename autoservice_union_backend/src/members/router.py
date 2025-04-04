import json

from fastapi import APIRouter, Depends
from starlette.requests import Request

from logger import logger


router = APIRouter(
    prefix="/api/members",
    tags=["survey"]
)


@router.post("/")
async def create_member(
    request: Request
):
    try:
        payload = await request.json()
        logger.info(json.dumps(payload))
    except Exception as e:
        logger.debug(e)
    finally:
        return {"ok: True"}