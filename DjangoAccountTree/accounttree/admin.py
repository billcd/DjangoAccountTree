from django.contrib import admin
from .models import Account


class AccountAdminInline(admin.TabularInline):

    model = Account
    fk_name = 'parent'
    list_display = ('name', '__str__',)
    fields = ('name', 'slug', 'user',)
    extra = 0


class AccountAdminClients(admin.ModelAdmin):

    module = Account
    list_filter = ( 'owner', 'active', 'type',)
    list_display = ('name',  '__str__',)
    ordering = ['name']
    search_fields = ('name',)
    inlines = [
        AccountAdminInline,
    ]


admin.site.register(Account, AccountAdminClients)
