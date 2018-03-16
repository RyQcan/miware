# coding:utf-8
from django.http import HttpResponse
from django.shortcuts import render

from midapp.models import Sitedata, IMG

from .mongoquery.mongo_settings import MONGO_SETTINGS
from .mongoquery.mongoquery import MongoQuery
import json
from pprint import pprint

def sitedataadd(request):
    site = request.POST['site']
    url = request.POST['url']
    uuid = request.POST['uuid']
    header = request.POST['header']
    content = request.POST['content']
    Sitedata.objects.create(site=site, url=url, uuid=uuid, header=header, content=content)
    new_img = IMG(img=request.FILES['file'])
    new_img.save()

    return HttpResponse(url)

def jsonadd(request):
    dict_data = str(request.POST['dict_data'])
    query = MongoQuery(MONGO_SETTINGS)

    ret = query.query(dict_data)
    pprint(json.loads(ret))
    return HttpResponse(ret)




