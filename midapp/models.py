from django.db import models

class Sitedata(models.Model):
    site = models.CharField('域名', max_length=30)
    url = models.CharField('网址', max_length=256)
    uuid = models.CharField('uuid', max_length=20, db_index=True)
    header = models.CharField('标题', max_length=256)
    content = models.TextField('内容', default='')

class IMG(models.Model):
    img = models.ImageField(upload_to='upload')