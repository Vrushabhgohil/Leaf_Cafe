from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from flask import Blueprint, redirect, render_template, request, url_for
from common.model import Product
from tenants.product import *
from tenants.users import *


admin_api  = Blueprint('admin_api',__name__,template_folder='templates',static_folder='static')
load_dotenv()
database_uri = os.getenv('DATABASE_URI')
engine = create_engine(database_uri)
Session = sessionmaker(bind=engine)
session = Session() 


# ADMIN DASHBOARD
@admin_api.route('/leafcafe/admin/dashboard/<string:tenant>')
def home(tenant):
    user = filter_user()
    product = filter_product()
    offer = filter_Offers()
    return render_template('admin/dashboard.html',tenant=tenant,user=user,product=product,offer=offer)

# ADD NEW PRODUCT
@admin_api.route('/leafcafe/admin/prodcuts/add/<string:tenant>',methods=['GET','POST'])
def add_product(tenant):
    if request.method == "POST":
        New_prduct()
        return redirect(url_for('admin_api.home',tenant=tenant))
    return render_template('admin/add_product.html',tenant=tenant)

# DELETE A PRODUCT
@admin_api.route('/leafcafe/admin/prodcuts/delete/<string:tenant>/<string:id>',methods=['GET','POST'])
def del_product(tenant,id):
    product = Product.query.get(id)
    del_product = db.session.delete(product)
    db.session.commit() 
    if del_product:
            return redirect(url_for('admin_api.products',tenant=tenant))
    return redirect(url_for('admin_api.products',tenant=tenant))

# UPDATE A PRODUCT
@admin_api.route('/leafcafe/admin/prodcuts/update/<string:tenant>/<string:id>',methods=['GET','POST'])
def update_product(id,tenant):
    product = Product.query.get(id)
    if request.method == 'POST':        
        updateProduct(product,id)
        return redirect(url_for('admin_api.products',tenant=tenant))
    return render_template('admin/update_product.html',tenant=tenant,product=product)

# DETAILS OF USER
@admin_api.route('/leafcafe/admin/user/profile/<string:tenant>/<string:id>')
def details_user(id,tenant):
    user = Users.query.get(id)
    return render_template('admin/user_details.html',tenant=tenant,user=user)

# BLOCK A USER
@admin_api.route('/leafcafe/admin/user/block/<string:tenant>/<string:id>')
def block_user(id,tenant):
    user = Users.query.get(id)
    user.user_status = "Block"
    user.is_active = False
    db.session.commit()
    return render_template('admin/user_details.html',tenant=tenant,user=user)


# LAUNCH NEW OFFER
@admin_api.route('/leafcafe/admin/offers/add/<string:tenant>',methods=['GET','POST'])
def add_offers(tenant):
    if request.method == "POST":
        New_offer()
        return redirect(url_for('admin_api.home',tenant=tenant))
    return render_template('admin/add_special.html',tenant=tenant)

# LIST OF ALL PRODUCTS
@admin_api.route('/leafcafe/admin/products/<string:tenant>')
def products(tenant):
    product = All_Product()
    return render_template('admin/products.html',tenant=tenant,product=product)

# LIST OF USERS
@admin_api.route('/leafcafe/admin/users/<string:tenant>')
def users(tenant):
    user = All_User()
    return render_template('admin/users.html',tenant=tenant,user=user)

