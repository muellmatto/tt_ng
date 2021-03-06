# Generated by Django 3.1.2 on 2020-10-14 17:22

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.embeds.blocks
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0012_auto_20201014_1715'),
    ]

    operations = [
        migrations.AlterField(
            model_name='webpage',
            name='body',
            field=wagtail.core.fields.StreamField([('paragraph', wagtail.core.blocks.RichTextBlock(features=['h1', 'h2', 'bold', 'italic', 'link', 'align_center', 'align_right', 'strikethrough', 'image'])), ('HTML', wagtail.core.blocks.RawHTMLBlock()), ('Embedded', wagtail.embeds.blocks.EmbedBlock()), ('Picture_variable', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock()), ('size', wagtail.core.blocks.IntegerBlock(default=100, label='Größe in Prozent', max_value=100, min_value=1))])), ('Multiple_pictures', wagtail.core.blocks.ListBlock(wagtail.images.blocks.ImageChooserBlock(), label='Mehrere Bilder Nebeneinander'))]),
        ),
    ]
