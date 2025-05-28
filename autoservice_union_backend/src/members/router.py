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
        data = await request.body()
        logger.info(f"Received request: {data}")
        json_data = json.loads(data)
        logger.info(json_data)
    except Exception as e:
        logger.debug(e)
    try:
        payload = await request.json()
        logger.info(payload)
    except Exception as e:
        logger.debug(e)
    finally:
        return {"ok: True"}