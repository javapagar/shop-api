from fastapi import FastAPI

from api.domain.tags import Tags, tags_info
from api.routers import cart


app = FastAPI(title="shopAPI", openapi_tags=tags_info)

app.include_router(cart.router)


@app.get(
    "/", tags=[Tags.HEALTH], name="Health", description="Check if the service is up"
)
async def check():
    return {"message": "All is fine!"}
