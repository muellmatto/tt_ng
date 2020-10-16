import wagtail.admin.rich_text.editors.draftail.features as draftail_features
from wagtail.admin.rich_text.converters.html_to_contentstate import (
    BlockElementHandler,
    InlineStyleElementHandler
)
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

@hooks.register('register_rich_text_features')
def enable_h1right_feature(features):
    control = {
        'type': 'h1_align_right',
        'label': 'H1⇥',
        'description': 'h1 text-align right',
        'element': 'h1',
        'style': {'text-align': 'right'},
    }
    features.register_editor_plugin (
        'draftail', 'h1_align_right', draftail_features.BlockFeature(control)
    )
    db_conversion = {
        'from_database_format': {
            'h1[class=align_right]': BlockElementHandler('h1_align_right')
        },
        'to_database_format': {
            'block_map': {
                'h1_align_right': {
                    'element': 'h1',
                    'props': {'class': 'align_right'}
                }
            }
        },
    }
    features.register_converter_rule('contentstate', 'h1_align_right', db_conversion)

@hooks.register('register_rich_text_features')
def enable_h1center_feature(features):
    control = {
        'type': 'h1_align_center',
        'label': 'H1→←',
        'description': 'h1 text-align center',
        'element': 'h1',
        'style': {'text-align': 'center'},
    }
    features.register_editor_plugin (
        'draftail', 'h1_align_center', draftail_features.BlockFeature(control)
    )
    db_conversion = {
        'from_database_format': {
            'h1[class=align_center]': BlockElementHandler('h1_align_center')
        },
        'to_database_format': {
            'block_map': {
                'h1_align_center': {
                    'element': 'h1',
                    'props': {'class': 'align_center'}
                }
            }
        },
    }
    features.register_converter_rule('contentstate', 'h1_align_center', db_conversion)

@hooks.register('register_rich_text_features')
def enable_h2right_feature(features):
    control = {
        'type': 'h2_align_right',
        'label': 'H2⇥',
        'description': 'h1 text-align right',
        'element': 'h2',
        'style': {'text-align': 'right'},
    }
    features.register_editor_plugin (
        'draftail', 'h2_align_right', draftail_features.BlockFeature(control)
    )
    db_conversion = {
        'from_database_format': {
            'h2[class=align_right]': BlockElementHandler('h2_align_right')
        },
        'to_database_format': {
            'block_map': {
                'h2_align_right': {
                    'element': 'h2',
                    'props': {'class': 'align_right'}
                }
            }
        },
    }
    features.register_converter_rule('contentstate', 'h2_align_right', db_conversion)

@hooks.register('register_rich_text_features')
def enable_h2center_feature(features):
    control = {
        'type': 'h2_align_center',
        'label': 'H2→←',
        'description': 'h2 text-align center',
        'element': 'h2',
        'style': {'text-align': 'center'},
    }
    features.register_editor_plugin (
        'draftail', 'h2_align_center', draftail_features.BlockFeature(control)
    )
    db_conversion = {
        'from_database_format': {
            'h2[class=align_center]': BlockElementHandler('h2_align_center')
        },
        'to_database_format': {
            'block_map': {
                'h2_align_center': {
                    'element': 'h2',
                    'props': {'class': 'align_center'}
                }
            }
        },
    }
    features.register_converter_rule('contentstate', 'h2_align_center', db_conversion)

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


@hooks.register('register_rich_text_features')
def enable_colored_feature(features):
    control = {
        'type': 'colored',
        'label': 'colored',
        'description': 'colored text',
        'style': {
            'color': 'orange'
        },
    }
    features.register_editor_plugin (
        'draftail', 'colored', draftail_features.InlineStyleFeature(control)
    )
    db_conversion = {
        'from_database_format': {
            'span[class=colored]': InlineStyleElementHandler('colored')
        },
        'to_database_format': {
            'style_map': {
                'colored': {
                    'element': 'span',
                    'props': {'class': 'colored'}
                }
            }
        },
    }
    features.register_converter_rule('contentstate', 'colored', db_conversion)

