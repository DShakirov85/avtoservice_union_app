from fastapi import FastAPI
from members.router import router as members_router


app = FastAPI(
    docs_url='/api/openapi',
    openapi_url='/api/openapi.json'
)

app.include_router(members_router)