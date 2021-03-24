from django.contrib import admin

from .models import Comment


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'comment', 'user', 'approved', 'created')
    search_fields = ('comment',)
    list_filter = ('approved',)
    date_hierarchy = 'created'
