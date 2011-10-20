"""Base classes for the CMS admin interface."""

from django.contrib import admin

import reversion


class AuditBaseAdmin(admin.ModelAdmin):
    
    """Base class for audited models."""
    
    list_display = ("__unicode__", "date_modified",)
            

class PublishedBaseAdmin(AuditBaseAdmin):
    
    """Base admin class for published models."""
    
    list_display = ("__unicode__", "is_online", "date_modified",)
    
    actions = ("publish_selected", "unpublish_selected",)
    
    change_form_template = "admin/core/publishedmodel/change_form.html"
    
    list_filter = ("is_online",)
    
    # Custom admin actions.
    
    def publish_selected(self, request, queryset):
        """Publishes the selected models."""
        queryset.update(is_online=True)
    publish_selected.short_description = "Place selected %(verbose_name_plural)s online"
    
    def unpublish_selected(self, request, queryset):
        """Unpublishes the selected models."""
        queryset.update(is_online=False)
    unpublish_selected.short_description = "Take selected %(verbose_name_plural)s offline"


class EntityBaseAdmin(reversion.VersionAdmin, PublishedBaseAdmin):
    
    """Base admin class for EntityBase models."""


class PageBaseAdmin(EntityBaseAdmin):
    
    """Base admin class for PageBase models."""

    list_display = ("title", "is_online", "date_modified",)
    
    prepopulated_fields = {"url_title": ("title",),}
    
    search_fields = ("title",)