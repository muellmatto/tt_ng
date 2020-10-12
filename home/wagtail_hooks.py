import wagtail.admin.rich_text.editors.draftail.features as draftail_features
from wagtail.admin.rich_text.converters.html_to_contentstate import BlockElementHandler
from wagtail.core import hooks


@hooks.register('register_rich_text_features')
def enable_right_feature(features):
    control = {
        'type': 'align_right',
        'label': '⇥',
        'description': 'text-align right',
        'element': 'p',
        'style': {
            'display': 'block',
            'text-align': 'right',
            
        },
    }
    features.register_editor_plugin (
        'draftail', 'align_right', draftail_features.BlockFeature(control)
    )
    db_conversion = {
        'from_database_format': {
            'p[class=align_right]': BlockElementHandler('align_right')
        },
        'to_database_format': {
            'block_map': {
                'align_right': {
                    'element': 'p',
                    'props': {'class': 'align_right'}
                }
            }
        },
    }
    features.register_converter_rule('contentstate', 'align_right', db_conversion)
    features.default_features.append('align_right')

@hooks.register('register_rich_text_features')
def enable_center_feature(features):
    control = {
        'type': 'align_center',
        'label': '→←',
        'description': 'text-align center',
        'element': 'p',
        'style': {'text-align': 'center'},
    }
    features.register_editor_plugin (
        'draftail', 'align_center', draftail_features.BlockFeature(control)
    )
    db_conversion = {
        'from_database_format': {
            'p[class=align_center]': BlockElementHandler('align_center')
        },
        'to_database_format': {
            'block_map': {
                'align_center': {
                    'element': 'p',
                    'props': {'class': 'align_center'}
                }
            }
        },
    }
    features.register_converter_rule('contentstate', 'align_center', db_conversion)
    features.default_features.append('align_center')
