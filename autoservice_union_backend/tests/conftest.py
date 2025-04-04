import os
from typing import AsyncGenerator

import pytest
from httpx import AsyncClient, ASGITransport

from main import app


@pytest.fixture(scope="session")
async def ac() -> AsyncGenerator[AsyncClient, None]:
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as ac:
        yield ac


@pytest.fixture(autouse=True)
def change_cwd():
    os.chdir(os.path.dirname(os.path.abspath(__file__)) + '/../src')