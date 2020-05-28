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


def register_site(model, manager=None):
    """Register models to admin.py"""

    if manager:
        admin.site.register(model, manager)
    else:
        admin.site.register(model)


register_model = [(models.User, UserAdmin),
                  (models.CovidNews, Covid19NewsModelAdmin),
                  (models.IndiaFullCovidStats, None),
                  (models.FranceCovidStats, None),
                  (models.IranCovidStats, None),
                  (models.WorldCovidStats, None),
                  (models.ChinaCovidStats, None),
                  (models.TurkeyCovidStats, None),
                  (models.SpainCovidStats, None),
                  (models.GermanyCovidStats, None),
                  (models.UkraineCovidStats, None),
                  (models.UKCovidStats, None),
                  (models.RussiaCovidStats, None),
                  (models.IndiaCovid19Update, None),
                  (models.IndiaCovidStats, None),
                  (models.Covid19Query, None),
                  (models.Covid19QueryReplies, None),
                  ]


for model_to_reg, model_manager in register_model:
    register_site(model_to_reg, model_manager)
