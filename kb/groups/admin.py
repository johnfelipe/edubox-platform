from django.contrib import admin
from .models import *

admin.site.register(Group)
admin.site.register(Institute)
admin.site.register(Role)
admin.site.register(Membership)