from django.db import models
from wagtail.models import Page
from wagtail.admin.panels import FieldPanel, MultiFieldPanel
from wagtail.fields import RichTextField
from wagtail.images.models import Image
from wagtail.search import index
from wagtail.fields import StreamField
from wagtail import blocks
from wagtail.images.blocks import ImageChooserBlock

class BlogIndexPage(Page):
    pass


class BlogPage(Page):

    description = RichTextField(
        max_length=255,
        null=True,
        blank=True
    )

    header_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    content = StreamField([
        ('heading', blocks.CharBlock(form_classname="title")),
        ('paragraph', blocks.RichTextBlock()),
        ('image', ImageChooserBlock()),
    ], use_json_field=True, default="")

    feed_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    # Editor panels configuration
    content_panels = Page.content_panels + [
        FieldPanel('description'),
        FieldPanel('header_image'),
        FieldPanel('content'),
    ]

    # Search index configuration
    search_fields = Page.search_fields + [
        index.SearchField('content'),
        # index.FilterField('date'),
    ]

    promote_panels = [
        MultiFieldPanel(Page.promote_panels, "Common page configuration"),
        FieldPanel('feed_image'),
    ]





