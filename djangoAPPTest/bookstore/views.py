from django.shortcuts import render
from django.http import HttpResponse
from . import models

# Create your views here.
def add_data(request):
    if request.method == "GET":
        try:
            models.Book.objects.create(title="西游记",price=60)
            del_obj = models.Book.objects.get(id=3)
            del_obj.delete()
        except Exception as e:
            return HttpResponse('导入失败：{}'.format(e))
        else:
            return HttpResponse("导入数据成功")
