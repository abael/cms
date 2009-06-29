"""Admin settings used by the news application."""


from django.contrib import admin

from cms.apps.pages.admin import site, ArticleBaseAdmin
from cms.apps.events.models import Event


class EventAdmin(ArticleBaseAdmin):
    
    """Admin settings used by news articles."""
    
    date_hierarchy = "start_date"
    
    list_display = ("title", "start_date", "is_online", "is_featured",)
    
    list_filter = ("is_online", "is_featured",)
    
    content_fieldsets = (("Event content", {"fields": ("content", "summary",),}),)
    
    publication_fieldsets = (("Publication", {"fields": ("start_date", "end_date", "is_online", "is_featured"),}),)
    
    fieldsets = ((None, {"fields": ("title", "url_title", "events_feed",),},),) + content_fieldsets + publication_fieldsets + ArticleBaseAdmin.navigation_fieldsets + ArticleBaseAdmin.seo_fieldsets
    
    radio_fields = {"events_feed": admin.VERTICAL}
    
    
site.register(Event, EventAdmin)

