# main/models.py
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    # 如果需要添加额外字段，可以在这里定义
    pass