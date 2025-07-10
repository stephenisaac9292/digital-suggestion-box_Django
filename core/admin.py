from django.contrib import admin
from .models import Suggestion

@admin.register(Suggestion)
class SuggestionAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'status', 'submitted_by', 'is_anonymous', 'created_at')
    list_filter = ('category', 'status', 'is_anonymous')
    search_fields = ('title', 'description')
