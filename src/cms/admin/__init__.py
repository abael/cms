"""Core CMS admin functionality."""

from django.contrib.auth.models import User, Group

from usertools.admin import UserAdmin, GroupAdmin

from cms.admin.sites import AdminSite, PAGE_FROM_KEY, PAGE_FROM_SITEMAP_VALUE
from cms.admin.base import PageBaseAdmin, PublishedBaseAdmin, EntityBaseAdmin


site = AdminSite()


# Register the auth models.

site.register(User, UserAdmin)

site.register(Group, GroupAdmin)