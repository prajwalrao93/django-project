from django.contrib import admin
from django.contrib.auth.models import Group, User
from .models import Profile, Posts, Comment, Message

# Register your models here.
admin.site.unregister(Group)

#Mix profile into user
class ProfileInline(admin.StackedInline):
    model = Profile

# Extend user model
class UserAdmin(admin.ModelAdmin):
    model = User
    #Just display username on admin page
    fields = ["username", "email"]
    inlines = [ProfileInline]

#Unregister initial user
admin.site.unregister(User)
#Reregister User
admin.site.register(User, UserAdmin)
#Register Posts
admin.site.register(Posts)
#Register Comments
admin.site.register(Comment)
#Register Messages
admin.site.register(Message)
