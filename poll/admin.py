from django.contrib import admin
from poll.models import Poll, Choice

admin.site.register(Poll)
admin.site.register(Choice)
