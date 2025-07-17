# -*- coding: utf-8 -*-

{
    'name': 'School Management',
    'category': 'Extra Tools',
    'version': '17.0.1.0',
    # 'license': 'LGPL-3',
    'summary': 'School Management',
    'description': """
        School Management
    """,
    # 'author': '',
    'depends': ['web', 'mail'],
    'data': [
        'security/ir.model.access.csv',
        'views/student_view.xml',
        'views/teachers_view.xml',
        'views/subject_view.xml',
        'views/school_student_view.xml',
        'views/core.xml',
         ],
    'installable': True
}
