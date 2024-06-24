import pytest
from httpx import AsyncClient

from bittensor_test_task.builder import get_app

pytestmark = pytest.mark.anyio


@pytest.fixture(scope="session")
def user_app():
    return AsyncClient(app=get_app("user"), base_url="http://test-user")


@pytest.fixture(scope="session")
def worker_app():
    return AsyncClient(app=get_app("worker"), base_url="http://test-worker")


async def test_end_to_end_one_client(user_app):
    r = await user_app.post("/order")
    assert r.status_code == 200
