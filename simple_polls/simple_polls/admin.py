from django.contrib import admin
from simple_polls.models import Survey

#admin.site.register(Survey)

class SurveyAdmin(admin.ModelAdmin):
    list_display = ('fullname', 'email','rating','other_python_interests','pyladies_interest','coworking_interest','satisfied_with_the_talk')
    search_fields = ('fullname', 'email')
    #list_filter = ('fullname', 'email','rating','other_python_interests','pyladies_interest','coworking_interest','satisfied_with_the_talk')
    list_filter = ('rating','other_python_interests','pyladies_interest','coworking_interest','satisfied_with_the_talk')
    readonly_fields = ('email',)

admin.site.register(Survey, SurveyAdmin)
