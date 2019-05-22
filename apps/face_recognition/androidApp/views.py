from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
from androidApp.models import PicUpload


# Create your views here.
def index(request):
    return HttpResponse('Hello World')


def image_upload_handler(request):
    """
    上传图片获取
    :param request:
    :return:
    """
    # 1.获取上传图片
    pic = request.FILES['image']
    print(pic.name)

    # 2.创建一个文件
    save_path = '%s/androidApp/%s' % (settings.MEDIA_ROOT, pic.name)
    with open(save_path, 'wb') as f:
        # 3.获取上传文件的内容并写到创建的文件中
        for content in pic.chunks():
            f.write(content)

    # 4.在数据库中保存上传记录
    PicUpload.objects.create(face_pic='androidApp/%s' % pic.name)

    return HttpResponse('Upload Success!!!')
