{
    'name': 'Product Reviews',
    'version': '1.0',
    'summary': 'Permite a los clientes poner reseñas sobre productos comprados',
    'category': 'Sales',
    'author': 'TuNombre',
    'website': 'tusitioweb.com',
    'license': 'AGPL-3',
    'depends': ['sale', 'product', 'sales_team'],
    'data': [
        'security/ir.model.access.csv',
        'views/product_review_views.xml',
        'views/product_review_menu.xml',
    ],
    'images': [
        'static/description/icon.png',  # Ruta al archivo de icono
    ],
    'demo': [],
    'installable': True,
    'auto_install': False,
}
