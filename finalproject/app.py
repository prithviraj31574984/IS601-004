from email.policy import default
from flask import Flask, render_template,request , redirect , flash,url_for,session
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os
from datetime import datetime, date
from flask_login import LoginManager,UserMixin,login_required,current_user,login_user,logout_user
from numpy import product
from werkzeug.utils import secure_filename
from PIL import Image
import pymysql
from sqlalchemy.sql import func
pymysql.install_as_MySQLdb()
import auth
from flask_cors import CORS
from flask_admin.contrib.sqla import ModelView
from flask_admin import Admin


app= Flask(__name__)
app.config["SECRET_KEY"]="Ywurow503985403924482jfsoakldfjasdltu394qipoafjo48950wjsfpas;lkr04589"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///e_commerce_database.sqlite"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SESSION_PERMANENT"] = True
app.config["SESSION_TYPE"] = "filesystem"


db=SQLAlchemy(app)
Migrate(app,db)
CORS(app)
login_manager = LoginManager()


now = datetime.now()
login_manager.init_app(app)
login_manager.login_view="login"
admin = Admin(app)

@login_manager.user_loader
def load_user(userid):
    return User.query.get(userid)

# Products (id, name, description, category, stock,
# created, modified, unit_price, visibility [true, false])

basdir = os.path.abspath(os.path.dirname(__file__))
Upload_dir = basdir + "/static/images/"
Allowed = ['JPG' ,'jpj' , 'PNG', 'png']


class User(db.Model , UserMixin):
    id = db.Column(db.Integer , primary_key=True)
    name = db.Column(db.String(50), unique=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    role = db.Column(db.String(100), default='user')
    product = db.relationship("Orders", backref='user' , lazy=True)
    rating = db.relationship("Ratings", backref='user', lazy = True)
    visibility = db.Column(db.String(255), default='True')

    
class Products(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    description = db.Column(db.String(255), nullable = False)
    category = db.Column(db.String(255), nullable=False)
    stock = db.Column(db.Integer, nullable=False)
    unit_price = db.Column(db.Integer, nullable=False)
    visibility = db.Column(db.Boolean(), default=1)
    image = db.Column(db.String(255))
    created = db.Column(db.TIMESTAMP(), server_default=func.now())
    modified = db.Column(db.TIMESTAMP(), server_default=func.now(), onupdate=func.current_timestamp())
    owner_id = db.Column(db.Integer, db.ForeignKey("user.id", ondelete="CASCADE"), nullable=False)
    orderitems = db.relationship("OrderItems", backref='products' , lazy=True)
    rating = db.relationship("Ratings", backref="products", lazy=True)

# Orders table (id, user_id, created, total_price, address,
# payment_method, money_received)
class Orders(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete="CASCADE"), nullable=False)
    total_price = db.Column(db.Integer)
    address = db.Column(db.String(500))
    payment_method = db.Column(db.String(255))
    money_received = db.Column(db.Integer)
    created = db.Column(db.DateTime, default=date.today())
    orderitems = db.relationship("OrderItems", backref='orders' , lazy=True)

# OrderItems table (id, order_id, product_id, quantity, unit_price)

class OrderItems(db.Model):
    id = db.Column(db.Integer , primary_key = True, nullable=False)
    order_id = db.Column(db.Integer, db.ForeignKey('orders.id', ondelete="CASCADE"), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('products.id', ondelete="CASCADE"), nullable=False)
    quantity = db.Column(db.Integer)
    unit_price = db.Column(db.Integer)


# d Ratings (id, product_id, user_id, rating, comment,
# created, modified)
class Ratings(db.Model):
    id = db.Column(db.Integer, primary_key = True, nullable= False)
    product_id = db.Column(db.Integer, db.ForeignKey('products.id', ondelete="CASCADE"), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete="CASCADE"), nullable=False)
    rating = db.Column(db.Integer)
    comment = db.Column(db.String(255))
    created = db.Column(db.TIMESTAMP(), server_default=func.now())
    modified = db.Column(db.TIMESTAMP(), server_default=func.now(), onupdate=func.current_timestamp())



def MergeDict(dict1, dict2):
    if isinstance(dict1, list) and isinstance(dict2, list):
        return dict1 + dict2
    elif isinstance(dict1, dict) and isinstance(dict2, dict):
        return dict(list(dict1.items()) + list(dict2.items()))



@app.route("/rating_product", methods=["GET","POST"])
@login_required
def rating_product():
    if request.method == "POST":
        product_id = request.form.get('product_id')
        rating = request.form.get("item_check")
        msg = request.form.get('msg')

        if rating == None:
            rating = 0

        if msg == "":
            return {"msg":"Please put some comment"}
    
        rating = Ratings(
            product_id = product_id,
            user_id = current_user.id,
            rating = rating,
            comment = msg
            )
        db.session.add(rating)
        db.session.commit()
        print("success")
        return {"success":"done"}
    


@app.route("/profile", methods = ['GET','POST'])
@login_required
def profile():
    row_per_page = 10
    page = request.args.get('page', 1, type=int)
    order = Orders.query.filter_by(user_id = current_user.id).order_by(Orders.created.desc()).paginate(page = page, per_page = row_per_page)
    if request.method == "POST":
        name = request.form['name']
        email = request.form['email']
        user = User.query.filter_by(email = current_user.email).first()
        user.name = name
        user.email = email
        db.session.commit()
    users = User.query.all()
    return render_template("profile.html", order = order, users = users)


@app.route("/history")
@login_required
def history():
    if current_user.role == 'user':
        flash("Please login as a admin to Access this page")
        return redirect('/login')
    row_per_page = 10
    page = request.args.get('page', 1, type=int)
    order = Orders.query.order_by(Orders.created.desc()).paginate(page = page, per_page = row_per_page)
    users = User.query.all()
    return render_template("dashboard/pages/orders_history.html", order = order, users = users)


@app.route("/confirmation/<id>")
@login_required
def confirmation(id):
    try:
        print(session['SHOP'])
    except Exception as e:
        print(e)
    order = db.session.query(OrderItems, Products).join(Products, OrderItems.product_id == Products.id, isouter=True).filter(OrderItems.order_id == id).all()
    print(type(order))
    total_price = 0
    for r in order:
        print(r[1].name , r[0].quantity, r[0].unit_price, r[1].image)
        total_price += r[0].unit_price
    data = Orders.query.filter_by(id = id).first()
    return render_template("order_confirmation.html", order = order, data = data, total_price = total_price)


@app.route("/checkout", methods=["GET","POST"])
@login_required
def checkout():
    try:
        product = session['SHOP']
    except:
        product = {}
    total_price = 0
    for key in product:
        total_price += product[key]['price']
#ucid-pg79
    if request.method =="POST":
        total_price = 0
        if 'SHOP' in session:
            for key in session['SHOP']:
                total_price += session['SHOP'][key]['price']    
        # cash, paymentMethod,zip,state,country, address2, address, email, name
        name = request.form['first_name']
        email = request.form['email']
        address = request.form['address']
        address2 = request.form['address2']
        country = request.form['country']
        state = request.form['state']
        zip = request.form['zip']
        paymentMethod = request.form['paymentMethod']
        cash = request.form['cash']
        complete_address = address+ " " + address2 + " " + country + " " + state + " " + zip
        data = Orders(
            user_id = current_user.id,
            total_price = total_price,
            address = complete_address,
            payment_method = paymentMethod,
            money_received = cash
        )
        db.session.add(data)
        db.session.commit()
        db.session.refresh(data)

        # DictItems = {product_id:{"name":product.name, "price":product.unit_price, "description":product.description, "image":product.image, "quantity":1}}
        # if 'SHOP' in session:
        #     product = session['SHOP']
        for value in product:
            Items = OrderItems(
                order_id = data.id,
                product_id = value,
                quantity = product[value]['quantity'],
                unit_price = product[value]['price']
            )
            db.session.add(Items)
            db.session.commit() 

        for value in product:
            print()
            P_data = Products.query.filter_by(id = value).first()
            P_data.stock -= product[value]['quantity']
            db.session.commit()

        session.pop('SHOP', None)
        session.modified = True 
        return redirect("/confirmation/"+ str(data.id))
    return render_template('checkout.html', product = product, total_price = total_price)


@app.route("/")
def home():
    try:
        cart_data = session['SHOP']
        print('==============================================================================')
        print(cart_data)
        print('----------------------------------------------------------------------------')
    except:
        cart_data = {}
    row_per_page = 10
    page = request.args.get('page', 1, type=int)
    product = Products.query.filter_by(visibility = 1).paginate(page = page, per_page=row_per_page)
    return render_template("index.html", product = product, cart_data = cart_data)


@app.route("/signup", methods=["POST","GET"])
def singup():
    if request.method == "POST":
        user_name = request.form.get('user_name')
        email = request.form.get("email")
        password = request.form.get('password')
        r_password = request.form.get("r_password")
        role = request.form.get('roles')
        type = request.form.get('type')
        

        if type == "Public":
            type = "True"
        else:
            type = "False"
        
        print(type)
        if role.lower() != 'admin':
            role = 'user'
        else:
            role='admin'
        
        if password != r_password:
            return {"password": "password not matched"}
        user = User.query.filter_by(name = user_name).first()
        
        if user:
            return {"user": "User Already Exists!"}
        email_checkup = User.query.filter_by(email = email).first()

        if email_checkup:
            return {"email": "Email Already Exists!"}

        print("done1")
        hashed_password = auth.hash(password)
        user_to_add = User(
            name = user_name,
            email = email,
            password = hashed_password,
            role = role,
            visibility = type
        )
        db.session.add(user_to_add)
        db.session.commit()    
        return {"msg":"created"}
    return render_template("signup.html")



@app.route("/login", methods = ['GET','POST'])
def login():
    if request.method == "POST":
        email = request.form.get('email')
        password = request.form.get('password')
        user = User.query.filter_by(email = email).first()
        if user:
            if auth.verify(password, user.password):
                login_user(user)
                return redirect("/")
            else:
                flash("Incorrect Password!")
                return redirect("/login")
        else:
            flash("No User found with this Email")
            return redirect("/login")
    return render_template("login.html")



@app.route("/delete/<id>")
@login_required
def delete_item(id):
    product = Products.query.filter_by(id = id).first()
    db.session.delete(product)
    db.session.commit()
    return redirect("/admin_dashboard")

@app.route("/admin_dashboard")
@login_required
def admin_dashboard():
    if current_user.role == 'user':
        flash("Please login as a admin to Access this page")
        return redirect('/login')
    product = Products.query.all()
    return render_template("dashboard/index.html", product = product)



@app.route("/add_post", methods=['GET','POST'])
@login_required
def add_post():
    if current_user.role == 'user':
        flash("Please login as a admin to Access this page")
        return redirect('/login')
    if request.method == "POST":
        name = request.form.get("name")
        description = request.form.get('description')
        category = request.form.get("category")
        stock = request.form.get("stock")
        unit_price = request.form.get('unit_price')
        visibility = request.form.get('visibility')
        file = request.files['image']
        filename = secure_filename(file.filename)

        if visibility.lower() == 'true':
            visibility = 1
        else:
            visibility = 0
        data = Products(
            name = name,
            description = description,
            category = category,
            stock = stock,
            unit_price = unit_price,
            visibility = visibility,
            image = filename,
            owner_id = current_user.id
            )

        print(filename.split('.')[1])
        if str(filename.split('.')[1]) not in Allowed:
            flash("Product Updated Succesfully ")
        file.save(os.path.join(Upload_dir, filename))
        print(file)
        db.session.add(data)
        db.session.commit()
        return redirect("/add_post")
        # print(name,description, stock, unit_price, visibility)
    return render_template("dashboard/pages/tables.html")



@app.route("/update/<id>", methods=["POST","GET"])
@login_required
def update(id):
    if current_user.role == 'user':
        flash("Please login as a admin to Access this page")
        return redirect('/login')
    update = 'yes'
    product = Products.query.filter_by(id = id).first()
    if request.method == "POST":
        name = request.form.get("name")
        description = request.form.get('description')
        category = request.form.get("category")
        stock = request.form.get("stock")
        unit_price = request.form.get('unit_price')
        visibility = request.form.get('visibility')
        file = request.files['image']
        print(file.filename)
        if file.filename == "":
            print("Yessssssssssssssssssssssssssssssssssssssssssssssssssssssssssssss")
            filename = product.image
        else:
            print("nonnn--------------------------------------")
            filename = secure_filename(file.filename)
            print(filename.split('.')[1])
            if str(filename.split('.')[1]) not in Allowed:
                flash("Product updates Succesfully !")
            file.save(os.path.join(Upload_dir, filename))

        if visibility.lower() == 'true':
            visibility = 1
        else:
            visibility = 0
        product.name = name
        product.description = description
        product.category = category
        product.stock = stock
        product.unit_price = unit_price
        product.visibility = visibility
        product.image = filename
        db.session.commit()
        return redirect("/admin_dashboard")
    return render_template("/dashboard/pages/tables.html", update = update, product = product)


@app.route("/products")
def products():
    try:
        cart_data=session['SHOP']
    except:
        cart_data = {}
    row_per_page = 3

    page = request.args.get('page', 1, type=int)
    product = Products.query.paginate(page=page, per_page=row_per_page)
    return render_template("product.html", product = product, cart_data = cart_data)


@app.route("/pro_cat/<id>")
def pro_cat(id):
    row_per_page = 10
    page = request.args.get('page', 1, type=int)
    cat = 'true'
    if id == "2":
        category = 'Caps'    
    if id == "1":
        category = "dresses"    
    if id == "3":
        category = "Computers"
    product = Products.query.filter_by(category = category).paginate(page=page, per_page=row_per_page)
    return render_template("product.html", product = product, id = id, cat = cat)



@app.route("/search", methods=["GET","POST"])
def Search():
    row_per_page = 10
    page = request.args.get('page', 1, type=int)
    result = request.form['search']
    product = Products.query.filter(Products.name.contains(result)).paginate(page=page, per_page=row_per_page)
    return render_template("product.html", product = product, result = result)


@app.route("/product_sort")
def product_sort():
    row_per_page = 10
    page = request.args.get('page', 1, type=int)
    product = Products.query.order_by(Products.unit_price.desc()).paginate(page=page, per_page=row_per_page)
    sort = "true"
    return render_template("product.html", product= product, sort = sort)


@app.route("/details/<id>")
def product_details(id):
    row_per_page = 10
    page = request.args.get('page', 1, type=int)
    rating = Ratings.query.filter_by(product_id=id).paginate(page = page , per_page = row_per_page)
    product = Products.query.filter_by(id = id).first()
    user = User.query.all()
    return render_template("details.html", product = product, rating = rating, user = user)

@app.route("/bulk_delete")
@login_required
def bulk_delete():
    products = Products.query.all()
    for product in products:
        db.session.delete(product)
        db.session.commit()
    return redirect("/admin_dashboard")


@app.route("/show_cart")
@login_required
def show_cart():
    try:
        cart_data = session['SHOP']
    except:
        cart_data = {}
    total_price = 0
    for key in cart_data:
        total_price += cart_data[key]['price']
    return render_template("cart.html", cart_data = cart_data, total_price=total_price)


@app.route("/cart_item_delete/<key>")
@login_required
def delete_session_item(key):
    if 'SHOP' in session:
        session['SHOP'].pop(key)
        session.modified = True
    return redirect('/show_cart')


@app.route("/cart", methods=['GET','POST'])
@login_required
def add_to_cart():
    if request.method == "POST":
        product_id = request.form.get('product_id')
        product = Products.query.filter_by(id = product_id).first()

        DictItems = {product_id:{"name":product.name, "price":product.unit_price, "description":product.description, "image":product.image, "quantity":1}}
        if "SHOP" in session:
            if  product_id in session['SHOP']:
                print("item id alreadys exists")
            else:
                session['SHOP']=MergeDict(session['SHOP'], DictItems)
        else:
            session['SHOP'] = DictItems

        if "SHOP" in session:
            print(session['SHOP'])

        data = session['SHOP']

        datas = len(data)
        return {"value":datas}


@app.route("/cart+", methods=["POST","GET"])
@login_required
def cart():
    if request.method == "POST":
        car_val = int(request.form.get('item_value'))
        price = float(request.form.get("price"))
        id = request.form.get("product_id")
        prod_price = float(request.form.get("prod_price"))
        product = Products.query.filter_by(id = id).first()
        if car_val >= product.stock:
            if 'SHOP' in session:
                session['SHOP'][id]['quantity'] = car_val
                session['SHOP'][id]['price'] = prod_price
                session.modified = True
            return {"val": car_val, "total_price":price, "prod_p":prod_price, "grand_total":price + 5}

        car_val += 1
        price += product.unit_price

        prod_price += product.unit_price
        if "SHOP" in session:
            session['SHOP'][id]['quantity'] = car_val
            session['SHOP'][id]['price'] = prod_price
            session.modified = True

        return {"val":car_val, "total_price":price, "prod_p":prod_price, "grand_total":price + 5}
    return render_template("cart.html")


@app.route("/cart-", methods=['GET',"POST"])
@login_required
def car_minus():
    if request.method == "POST":
        car_val = int(request.form.get("item_value"))
        price = float(request.form.get("price"))
        id = request.form.get("product_id")
        prod_price = float(request.form.get("prod_price"))

        product = Products.query.filter_by(id = id).first()
        car_val -= 1
        if car_val == 0:
            if 'SHOP' in session:
                session['SHOP'][id]['quantity'] = 1
                session['SHOP'][id]['price'] = prod_price
                session.modified = True
            return {"val":1, "total_price":price, "prod_p":prod_price, "grand_total":price + 5}
        price -= product.unit_price
        prod_price -= product.unit_price
        if 'SHOP' in session:
            session['SHOP'][id]['quantity'] = car_val
            session['SHOP'][id]['price'] = prod_price
            session.modified = True

        return {"val":car_val, "total_price":float(price), "prod_p":prod_price, "grand_total":price + 5}


@app.route("/logout")
@login_required
def user_logout():
    logout_user()
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)
