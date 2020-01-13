from django.contrib import admin
from Ins.models import Post, InsUser, Like, Comment, UserConnection

# Register your models here.

class CommentInline(admin.StackedInline):
    model = Comment

class LikeInline(admin.StackedInline):
    model = Like

class FollowingInline(admin.StackedInline):
    model = UserConnection
    fk_name = 'creator'

class FollowerInline(admin.StackedInline):
    model = UserConnection
    fk_name = 'following'

class PostAdmin(admin.ModelAdmin):
    inlines = [
        CommentInline,
        LikeInline,
    ]

class UserAdmin(admin.ModelAdmin):
    inlines = [
        FollowerInline,
        FollowingInline,
    ]


admin.site.register(Post, PostAdmin)
admin.site.register(InsUser, UserAdmin)
admin.site.register(Like)
admin.site.register(Comment)
admin.site.register(UserConnection)