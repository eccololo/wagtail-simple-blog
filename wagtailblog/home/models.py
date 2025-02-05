from django.db import models

from wagtail.models import Page
from wagtail.admin.panels import FieldPanel, MultiFieldPanel
from wagtail.fields import RichTextField


class HomePage(Page):
    
    call_to_action = models.CharField(
        max_length=255,
        null=True,
        blank=True
    )

    description = RichTextField(
        null=True,
        blank=True
    )

    # Editor panels configuration
    content_panels = Page.content_panels + [
        # FieldPanel('header_image'),
        # FieldPanel('date'),
        FieldPanel("call_to_action"),
        FieldPanel('description'),
    ]
