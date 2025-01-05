from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from api.api_v1.queues.schemas import CreateQueue
from core.models.queue import Queue, QueueEntries
from utils.exception_handlers import average_handle_exception


async def create_queue(
    session: AsyncSession,
    queue_to_create: CreateQueue,
) -> Queue:
    try:
        # создаем модель и делаем запрос в базу данных
        queue = Queue(**queue_to_create.model_dump())
        session.add(queue)
        await session.commit()
        return queue

    # обработка ошибки
    except Exception as e:
        average_handle_exception(e)


async def get_queues(session: AsyncSession):
    try:
        # создаем запрос и делаем запрос в базу данных
        query = select(Queue)
        result = await session.execute(query)
        queues = result.scalars().all()
        return queues

    # обработка ошибки
    except Exception as e:
        average_handle_exception(e)


async def get_queue_with_entries(session: AsyncSession, queue_id: int):
    try:
        # создание запроса
        query = (
            select(Queue)
            .outerjoin(Queue.entries)  # Используем outerjoin для левого соединения
            .outerjoin(QueueEntries.user)
            .where(Queue.id == queue_id)
            .options(selectinload(Queue.entries).selectinload(QueueEntries.user))
        )

        # выполнения запроса
        result = await session.execute(query)
        queue_with_entries = result.scalars().first()
        return queue_with_entries

    # обработка ошибок
    except Exception as e:
        average_handle_exception(e)
