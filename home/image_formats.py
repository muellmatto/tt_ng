from wagtail.images.formats import Format, register_image_format, unregister_image_format

unregister_image_format('fullwidth')
register_image_format(Format('fullwidth', 'Full Width', 'richtext-image full-width', 'width-1200'))
