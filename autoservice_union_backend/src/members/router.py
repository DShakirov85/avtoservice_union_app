import json
from typing import Union

from fastapi import APIRouter, Depends
from starlette.background import BackgroundTask
from starlette.requests import Request

from logger import logger
from starlette.responses import JSONResponse

from .services import fix_bad_json, process_data



router = APIRouter(
    prefix="",
    tags=["survey"]
)


@router.post("/")
async def create_member(
    request: Request
):
    try:
        data = await request.body()
        j = json.loads(fix_bad_json(data))
        background_task =  BackgroundTask(process_data, j)
    except Exception as e:
        logger.info(e)
        background_task = None
    finally:
        return JSONResponse({"ok": True}, background=background_task)
