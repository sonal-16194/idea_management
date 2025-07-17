# -*- coding: utf-8 -*-

{
    'name': 'Idea Management',
    'category': 'Extra Tools',
    'version': '17.0.1.0',
    # 'license': 'LGPL-3',
    'summary': 'Idea Management',
    'description': """
        Idea Management
    """,
    # 'author': '',
    'depends': ['web', 'mail','project'],
    'data': [
        'security/ir.model.access.csv',
        'report/report_action.xml',
        'report/report_idea_template.xml',
        'views/idea_management.xml',
        'views/idea_create.xml',
        'views/task.xml',
        
        
         ],
    'installable': True,
    'application': True,
}
