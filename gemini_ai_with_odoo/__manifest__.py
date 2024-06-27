# -*- coding: utf-8 -*-
# Copyright (c) 2024-Present Namah Softech Pvt Ltd. (<https://namahsoftech.com//>)

{
    'name': "Gemini AI With Odoo",

    'summary': "Gemini AI Integration With Odoo",

    'description': """
    Gemini AI for Odoo Discuss is a handy tool that brings the power of AI directly into your communication channels.
    It lets you chat with me, Gemini, to get help with various tasks within Odoo Discuss. Imagine needing a creative
    spark for an email or wanting to quickly draft social media posts - just ask me! This free app can boost your 
    productivity and open up new possibilities, all within the familiar Odoo interface.
    """,

    'author': "Namah Softech Pvt Ltd",
    'maintainer': 'Namah Softech Pvt Ltd',
    'website': "https://namahsoftech.com/",
    'category': 'Extra Tools',
    'version': '17.0.1.0',
    'depends': ['base', 'base_setup', 'mail'],
    'external_dependencies': {'python': ['google-generativeai']},
    'data': [
        'security/ir.model.access.csv',
        'data/gemini_model_data.xml',
        'data/mail_channel_data.xml',
        'data/user_partner_data.xml',
        'views/res_config_settings_views.xml',
    ],
    'images': [
        'static/description/gemini_ai_odoo.png',
        'static/description/updated_discuss_ui.png',
        'static/description/text_images_to_text.png',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
