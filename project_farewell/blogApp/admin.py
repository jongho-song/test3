from django.contrib import admin

from .models import Blog # models.py에서 video를 import함

admin.site.register(Blog) # admin 사이트에 video DB 등록