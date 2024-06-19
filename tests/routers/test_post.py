import pytest
from httpx import AsyncClient


async def create_post(body: str, async_client: AsyncClient) -> dict:
    response = await async_client.post("/create_post", json={"body": body})
    return response.json()


async def create_comment(body: str, post_id: int, async_client: AsyncClient) -> dict:
    response = await async_client.post(
        "/comment", json={"body": body, "post_id": post_id}
    )
    return response.json()


@pytest.fixture()
async def created_post(async_client: AsyncClient):
    return await create_post("Test Post API", async_client)


@pytest.fixture()
async def created_comment(async_client: AsyncClient, created_post: dict):
    return await create_comment(
        "Test Post API Comment Route", created_post["id"], async_client
    )


@pytest.mark.anyio
async def test_create_post(async_client: AsyncClient):
    body = "Test Post"

    response = await async_client.post("/create_post", json={"body": body})

    assert response.status_code == 200
    assert {"id": 1, "body": body}.items() <= response.json().items()


@pytest.mark.anyio
async def test_create_post_missing_data(async_client: AsyncClient):

    response = await async_client.post("/create_post", json={})

    assert response.status_code == 422


@pytest.mark.anyio
async def test_get_all_posts(async_client: AsyncClient, created_post: dict):
    response = await async_client.get("/get_all_posts")

    assert response.status_code == 200
    assert response.json() == [created_post]


@pytest.mark.anyio
async def test_create_comment(async_client: AsyncClient, created_post: dict):
    body = "Test Post Comment"

    response = await async_client.post(
        "/comment", json={"body": body, "post_id": created_post["id"]}
    )

    assert response.status_code == 200
    assert {
        "id": 1,
        "body": body,
        "post_id": created_post["id"],
    }.items() <= response.json().items()


@pytest.mark.anyio
async def test_get_comments_on_post(
    async_client: AsyncClient, created_post: dict, created_comment: dict
):
    response = await async_client.get(f"/post/{created_post['id']}/comments")

    assert response.status_code == 200


@pytest.mark.anyio
async def test_get_comments_on_post_empty(
    async_client: AsyncClient, created_post: dict
):
    response = await async_client.get(f"/post/{created_post['id']}/comments")

    assert response.status_code == 200


@pytest.mark.anyio
async def test_get_post_with_comments(
    async_client: AsyncClient, created_post: dict, created_comment: dict
):
    response = await async_client.get(f"/post/{created_post['id']}")

    assert response.status_code == 200
