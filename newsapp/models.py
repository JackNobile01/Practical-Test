from django.db import models


class Article(models.Model):
    heading_text = models.CharField(max_length=100)
    pub_date_text = models.DateTimeField('Date Published:')
    body_text = models.CharField(max_length=400)