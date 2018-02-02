from django.db import models

# Create your models here.
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)

    nickname = models.CharField('微信昵称',max_length=100)
    openid = models.CharField('用户标识', max_length=100, default='default')
    cookie = models.CharField('用户认证标识', max_length=100,default='')

    GENDER = (
        (1,'男'),
        (2,'女'),
        (0,'未知')
    )

    gender = models.CharField('性别', max_length=10, choices=GENDER)

    def __str__(self):
        return self.nickname


class letter(models.Model):
    owner = models.CharField('发送者用户标识',max_length=100, default="default")
    letter = models.CharField('信件内容',max_length=600)

    STATUS = (
        (1, 'seccues'),
        (2, 'failed')
    )
    status = models.CharField('信件状态', max_length=10, choices=STATUS, default = 1)
    send_time = models.DateTimeField('信件发送时间',auto_now_add=True)
    to_user_id = models.CharField('收信者用户标识',max_length=100, default="default")
    record_url = models.URLField()
