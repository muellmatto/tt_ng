from django.db import models

from modelcluster.fields import ParentalKey

from wagtail.admin.edit_handlers import (
    FieldPanel,
    StreamFieldPanel, 
    PageChooserPanel
)

from wagtail.core import blocks
from wagtail.core.fields import RichTextField, StreamField
from wagtail.core.models import Page

from wagtail.embeds.blocks import EmbedBlock

from wagtail.images.blocks import ImageChooserBlock
from wagtail.images.edit_handlers import ImageChooserPanel

from wagtailmedia.edit_handlers import MediaChooserPanel

class StartPage(Page):
    show_in_menus_default = False
    max_count = 1
    parent_page_types = ['wagtailcore.page']
    picture =  models.ForeignKey(
        'wagtailimages.Image',
        null = True,
        blank = True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    video = models.ForeignKey (
        'wagtailmedia.Media',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    next_page = models.ForeignKey(
        'wagtailcore.Page',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    greeting = RichTextField(
        blank=True,
        null=True,
        features=[
            'h1',
            'h2',
            'bold',
            'italic',
            'link',
            'align_center',
            'align_right',
            'h1_align_center',
            'h1_align_right',
            'h2_align_center',
            'h2_align_right',
            'colored',
            'strikethrough'],
    )
    content_panels = Page.content_panels + [
        ImageChooserPanel('picture'),
        MediaChooserPanel('video'),
        FieldPanel('greeting'),
        PageChooserPanel('next_page')
    ]

class WebPage(Page):
    """ This is normal page"""
    show_in_menus_default = True
    parent_page_types = ['home.StartPage']
    body = StreamField (
        [
            ( 'paragraph', blocks.RichTextBlock(
                features=[
                    'h1',
                    'h2',
                    'bold',
                    'italic',
                    'link',
                    'align_center',
                    'align_right',
                    'h1_align_center',
                    'h1_align_right',
                    'h2_align_center',
                    'h2_align_right',
                    'colored',
                    'strikethrough',
                    'image'],
                )
            ),
            ( 'HTML', blocks.RawHTMLBlock() ),
            ( 'Embedded', EmbedBlock() ),
            ( 'Picture_variable', blocks.StructBlock([
                    ('image', ImageChooserBlock()),
                    ('size', blocks.IntegerBlock(
                        min_value=1,
                        max_value=100,
                        default=100,
                        label='Größe in Prozent'
                    )),
                ])
            ),
            ( 'Multiple_pictures', blocks.ListBlock(
                    ImageChooserBlock(),
                    label='Mehrere Bilder Nebeneinander'
                )
            )
        ]
    )
    content_panels = Page.content_panels + [
        StreamFieldPanel ( 'body' ),
    ]

class Gallery(Page):
    """ This page lists all works"""
    show_in_menus_default = True
    parent_page_types = ['home.StartPage']
    subpage_types = ['WorkPage']
    max_count = 1


class WorkPage(WebPage):
    """ works """
    parent_page_types = ['Gallery']
    subpage_types = []
    coverimage = models.ForeignKey(
        'wagtailimages.Image',
        null = True,
        blank = False,
        on_delete = models.SET_NULL,
        related_name = '+'
    )
    content_panels = [
        ImageChooserPanel('coverimage'),
    ] + WebPage.content_panels

