from tortoise import fields, models
from tortoise.contrib.pydantic import pydantic_model_creator


class Article(models.Model):
    id = fields.IntField(pk=True)
    title = fields.CharField(max_length=55)
    description = fields.CharField(max_length=255)


ArticlePydantic = pydantic_model_creator(Article, name='Article')
ArticleInPydantic = pydantic_model_creator(Article, name='ArticleIn')