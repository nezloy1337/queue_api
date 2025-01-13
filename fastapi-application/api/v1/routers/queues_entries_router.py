from typing import Annotated

from fastapi import APIRouter, HTTPException, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession

from api.v1.routers.auth.fastapi_users_routers import current_user
from api.v1.routers.queues_entries import crud
from core.models import db_helper, User
from schemas.queue_entries import CreateQueueEntry

router = APIRouter(
    prefix="",
    tags=["queues_entries"],
)


@router.post(
    "/queues/{queue_id}",
    response_model=CreateQueueEntry,
    status_code=status.HTTP_201_CREATED,
)
async def create_queue_entry(
    queue_entry_to_create: CreateQueueEntry,
    session: Annotated[AsyncSession, Depends(db_helper.session_getter)],
    user: Annotated[User, Depends(current_user)],
):
    return await crud.create_queues_entry(
        session,
        queue_entry_to_create,
        user,
    )


@router.delete(
    "/queue/{queue_id}",
)
async def delete_queue_entry(
    session: Annotated[AsyncSession, Depends(db_helper.session_getter)],
    user: Annotated[User, Depends(current_user)],
    queue_id: int,
):
    return await crud.delete_queues_entry(
        session,
        user,
        queue_id,
    )


@router.delete(
    "/queue/clear/{secret_code}",
)
async def clear_queue_entry(
    session: Annotated[AsyncSession, Depends(db_helper.session_getter)],
    secret_code: str,
):
    # заглушка чтобы любой абобус не мог удалить
    if secret_code == "admin132":
        return await crud.clear_queues_entry(session)
    else:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="обойдешься"
        )
