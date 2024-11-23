from fastapi import FastAPI

from app.api.v2.handlers import router


async def lifespan(_: FastAPI):
    yield


def init_app():
    app = FastAPI(
        title="Book collection",
        debug=False,
        version='0.0.1',
        docs_url='/docs',
        redoc_url='/redoc',
        lifespan=lifespan,
    )
    app.include_router(router)
    return app


app = init_app()
