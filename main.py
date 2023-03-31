from typing import List

from fastapi import FastAPI
from models import ArticlePydantic, ArticleInPydantic, Article
from tortoise.contrib.fastapi import HTTPNotFoundError, register_tortoise


app = FastAPI()


@app.get('/articles', response_model=List[ArticlePydantic])
async def get_article():
    return await ArticlePydantic.from_queryset(Article.all())



@app.get('/articles/{id}', response_model=ArticlePydantic, responses={404: {'model': HTTPNotFoundError}})
async def get_details(id: int):
    return await ArticlePydantic.from_queryset_single(Article.get(id=id))


@app.put('/articles/{id}', response_model=ArticlePydantic, responses={404: {'model': HTTPNotFoundError}})
async def update_article(id: int, article: ArticleInPydantic):
    await Article.filter(id=id).update(**article.dict(exclude_unset=True))
    await Article.save()

    return await ArticlePydantic.from_queryset_single(Article.get(id=id))


@app.post('/articles', response_model=ArticlePydantic)
async def add_article(article: ArticleInPydantic):
    article_obj = await Article.create(**article.dict(exclude_unset=True))

    return await ArticlePydantic.from_tortoise_orm(article_obj)


register_tortoise(
    app,
    db_url='postgres://home:123456@localhost/articles',
    modules={'models': ['models']},
    generate_schemas=True,
    add_exception_handlers=True
)
