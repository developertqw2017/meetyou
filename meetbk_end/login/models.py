from django.db import models

# Create your models here.
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User)

    nickname = models.CharField('微信昵称',max_length=100)
    openid = models.CharField('用户标识', max_leng, default='default')
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
    owner = models.ForeignKey('Profile',verbose_name="拥有者")
    letter = models.CharField('信件内容',max_length=600)

    STATUS = (
        (1, 'seccues'),
        (2, 'failed')
    )
    status = models.CharField('信件状态', max_length=10, choices=STATUS, default = 1)
    send_time = models.DateTimeField('信件发送时间',auto_now_add=True)
    to_user_id = models.ForeignKey('Profile',verbose_name="接收者")
    record = models.ForeignKey('record',verbose_name="录音")

class record(models.Model):
    record_url = models.URLField()
