# -*- coding: utf-8 -*-
{
    'name': "Project Scrum ",
    'version': "1.3",
    'author': "Cogitae",
    'category': "Project Scrum ",
    'summary': 'Projects, Scrum',
    'description': """
Scrum Module for OpenERP 7.0 developped by Cogitae


    """,
    
    'website': 'http://www.cogitae.net',
    'images': [],
    'depends': [
        'base',
        'mail',
        'project',
    ],
    'data': [
        "project_scrum_report.xml",
        "view/project_view.xml",
        
        "security/project_scrum_security.xml",
        "security/ir.model.access.csv",
        
        
        "wizard/project_scrum_backlog_create_task_view.xml",
        "wizard/project_scrum_email_view.xml",
        "wizard/user_story_sandbox_to_backlog_view.xml",
        
        "view/project_scrum_menu.xml",
        "view/project_scrum_release_view.xml",
        "view/project_scrum_role_view.xml",
        "view/project_scrum_sandbox_view.xml",
        "view/project_scrum_view.xml",
    ],
    'css': [
        'static/src/css/project_scrum.css',
    ],
    'demo': [],
    'test': [],
    'application': True,
    'installable': True,
    'auto_install': False,
    'web': True,
}
