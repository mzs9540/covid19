from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext as _

from . import models


class UserAdmin(BaseUserAdmin):
    ordering = ['id']
    list_display = ['email', 'name', 'country', 'phone']
    search_fields = ('email', 'name', 'phone', 'country')
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal Info'), {'fields': ('name', 'country', 'phone')}),
        (
            _('Permissions'),
            {'fields': ('is_active', 'is_superuser', 'is_staff')}
        ),
        (_('Important Dates'), {'fields': ('last_login',)})
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2')
        }),
    )


class Covid19NewsModelAdmin(admin.ModelAdmin):
    ordering = ['-date']
    list_display = ['title', 'date']
    search_fields = ('title', 'href')


admin.site.register(models.User, UserAdmin)
admin.site.register(models.CovidNews, Covid19NewsModelAdmin)
admin.site.register(models.IndiaCovidStats)
admin.site.register(models.WorldCovidStats)
