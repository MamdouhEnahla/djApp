from inspect import classify_class_attrs
from django.contrib import admin
from .models import *
# Register your models here.
admin.site.site_header ='Boards Control Panel'
admin.site.site_title = 'Boards Administration'

class InlineTopic(admin.TabularInline):
    model = Topic
    extra = 1

class BoardAdmin(admin.ModelAdmin):
    inlines = [InlineTopic]
    

class TopicAdmin(admin.ModelAdmin):
    fields = ('subject', 'board', 'views')
    list_display = ('subject', 'board', 'views')


admin.site.register(Board, BoardAdmin)
admin.site.register(Topic, TopicAdmin)
admin.site.register(Post)