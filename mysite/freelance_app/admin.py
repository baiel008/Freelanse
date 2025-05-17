from django.contrib import admin
from django.contrib.admin import TabularInline
from .models import *

admin.site.register(Skill)
admin.site.register(UserProfile)
admin.site.register(Category)
admin.site.register(Project)
admin.site.register(Offer)
admin.site.register(Review)