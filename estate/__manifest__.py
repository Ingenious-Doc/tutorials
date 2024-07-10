{
        'name':'Real Estate',
        'version':'0.01',
        'sequence':12,
        'summary': 'realestate application',
        'description':"",
        'website':'https://www.odoo.com/page/estate',
        'depends':['base'],
        'data':['security/ir.model.access.csv',
               'views/estate_property_views.xml','views/estate_property_offer.xml','views/estate_types.xml','views/estate_tags.xml' ,'views/estate_menus.xml',],
        'application':True,
        'installable':True
}
