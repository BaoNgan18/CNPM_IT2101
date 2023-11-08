from flask_admin import Admin
from app import db, app
from flask_admin.contrib.sqla import ModelView
from app.models import Category, Product

admin = Admin(app=app, name='Quan tri ban hang', template_mode='bootstrap4')

class ProductView(ModelView):
    column_list = ['id', 'name', 'price']
    can_export = True
    column_searchable_list = ['name']
    column_filters = ['name', 'price']
    column_editable_list = ['name', 'price']
    edit_modal = True


class CategoryView(ModelView):
    column_list = ['id', 'name', 'products']
    # can_export = True
    # column_searchable_list = ['name']
    # column_filters = ['name', 'products']
    # column_editable_list = ['name', 'products']
    # edit_modal = True

admin.add_view(CategoryView(Category, db.session))
admin.add_view(ProductView(Product, db.session))
