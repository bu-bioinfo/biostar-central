from django.contrib import admin
from .models import Profile, Logger

from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User


class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'Profile'
    fk_name = 'user'


@admin.register(Logger)
class LoggerAdmin(admin.ModelAdmin):
    list_display = ('action', 'user', 'target', 'date')
    ordering = ['-date']

    fieldsets =(("Details",
                  {"fields": ("user", 'log_text')}
                ),)

    search_fields = ('user__email', 'user__profile__name', 'user__profile__uid', 'log_text')


class CustomUserAdmin(UserAdmin):
    inlines = (ProfileInline, )
    list_display = ('email', 'first_name', 'is_staff', 'is_active', "get_state")
    list_select_related = ('profile', )

    fieldsets = (
        ("Information",
                  {"fields": ("username", "email", "password")}
                  ),
        ("Permissions",
                 {'fields': ("is_staff","is_active", "is_superuser"),
                     "classes": ('extrapretty')}
                  )
                 )

    def get_state(self, instance):
        return instance.profile.get_state_display()

    get_state.short_description = 'Status'

    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        return super(CustomUserAdmin, self).get_inline_instances(request, obj)

admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)