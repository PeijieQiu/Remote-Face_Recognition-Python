from django.db import models


# Create your models here.
class PicUpload(models.Model):
    face_pic = models.ImageField(upload_to='androidApp')  # 相对于media下的目录

