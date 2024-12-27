from contextlib import asynccontextmanager
from core.models import db_helper, Base
import uvicorn
from fastapi import FastAPI

from core.config import settings
from fastapi.responses import ORJSONResponse



@asynccontextmanager
async def lifespan(app: FastAPI):
    # startapp
    yield
    # shutdown
    await db_helper.dispose()


main_app = FastAPI(
    default_response_class=ORJSONResponse,
    lifespan=lifespan,
)



if __name__ == "__main__":
    uvicorn.run(
        "main:main_app",
        host=settings.run.host,
        port=settings.run.port,
        reload=True,
    )
