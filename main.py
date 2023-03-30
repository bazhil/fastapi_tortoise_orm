from fastapi import FastAPI
from models import ArticlePydantic, ArticleInPydantic
from tortoise.contrib.fastapi import HTTPNotFoundError, register_tortoise


app = FastAPI()


@app.get('/')
async def get_article():
    return {'message': 'working'}


register_tortoise(
    app,
    db_url='postgresql://home:123456@localhost/articles',
    modules={'models': ['api.models']},
    generate_schemas=True,
    add_exception_handlers=True
)
