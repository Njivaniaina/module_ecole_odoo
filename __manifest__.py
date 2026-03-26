{
    'name': 'Gestion École',
    'version': '17.0.1.0.0',
    'summary': 'Gestion des étudiants, cours et notes',
    'author': 'Fenosoa',
    'category': 'Education',
    'depends': ['base', 'mail'],
    'data': [
        'security/ir.model.access.csv',
        'data/sequences.xml', 
        'views/etudiant_views.xml',
        'views/cours_views.xml',
        'views/note_views.xml',
        'views/enseignant_views.xml',
        'data/demo_data.xml',
    ],
    'installable': True,
    'application': True,
}