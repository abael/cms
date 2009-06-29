"""Models used by the news publication application."""


import datetime

from django.db import models

from cms.apps.pages.models import Page, ArticleBase, PageField, HtmlField, PageBaseManager, PublishedPageManager


class Article(ArticleBase):
    
    """A news article."""
    
    publication_clause = "is_online = TRUE AND publication_date <= TIMESTAMP('%(now)s')"
    
    news_feed = PageField(Page,
                          "newsfeed")
    
    content = HtmlField(blank=True,
                        null=True)
    
    summary = models.TextField(blank=True,
                               null=True,
                               help_text="A short summary of this article.  This will be used on news pages and RSS feeds.  If not specified, then a summarized version of the content will be used.")
    
    # Publication fields.
    
    publication_date = models.DateField(default=lambda: datetime.datetime.now().date(),
                                        help_text="The date that this article will appear on the website.")
    
    is_featured = models.BooleanField("featured",
                                      default=False,
                                      help_text="Featured articles will remain at the top of any news feeds.")
    
    def get_absolute_url(self):
        """Returns the absolute URL of the article."""
        return self.news_feed.content.reverse("article_detail", self.publication_date.year, self.publication_date.month, self.url_title)
    
    class Meta:
        verbose_name = "news article"
        unique_together = (("news_feed", "url_title",),)
        ordering = ("-is_featured", "-publication_date", "-id")

