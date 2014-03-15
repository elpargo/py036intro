from django.contrib import admin
from simple_polls.models import Survey

#admin.site.register(Survey)

class SurveyAdmin(admin.ModelAdmin):
    pass
admin.site.register(Survey, SurveyAdmin)
