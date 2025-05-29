import ast
import json

from fastapi import APIRouter, Depends
from starlette.requests import Request

from logger import logger
from .services import fix_bad_json


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
        print(data)
        j = json.loads(fix_bad_json(data))
        print(j)
    except Exception as e:
        print(e)
    finally:
        return {"ok": True}
