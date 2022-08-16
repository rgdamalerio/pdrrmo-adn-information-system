from django.contrib import admin
from users.models import UserProfile
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as AuthUserAdmin

# Register your models here.
class UserProfileInline(admin.StackedInline):
  model = UserProfile
  can_delete: False

class AccountsUserAdmin(AuthUserAdmin):
  inlines = [UserProfileInline]

admin.site.unregister(User)
admin.site.register(User,AccountsUserAdmin)