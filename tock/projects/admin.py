from django.contrib import admin

from .models import Agency, Project, ProfitLossAccount, ProjectAlert, AccountingCode


class AgencyAdmin(admin.ModelAdmin):
    search_fields = ['name',]


class AccountingCodeAdmin(admin.ModelAdmin):
    search_fields = ['agency__name', 'office',]

class ProfitLossAccountAdmin(admin.ModelAdmin):
    search_fields = ['name',]

class ProjectAdmin(admin.ModelAdmin):
    search_fields = ['name',]

class ProjectAlertAdmin(admin.ModelAdmin):
    search_fields = ['title',]


admin.site.register(Agency, AgencyAdmin)
admin.site.register(AccountingCode, AccountingCodeAdmin)
admin.site.register(ProfitLossAccount, ProfitLossAccountAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(ProjectAlert, ProjectAlertAdmin)
