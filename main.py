from flask import Flask, request, render_template, redirect, url_for, session
from models import db, User, Role, Morada, Carrinho, Produto

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///pw.db"
app.config['SECRET_KEY'] = 'secret_key'
db.init_app(app)

@app.route("/")
def index():
    products = Produto.query.all()
    return render_template("index.html", products=products)

@app.route('/adiciona', methods=['POST'])
def add_item():
    username = session['user']
    # Query the database to get the user's profile information
    user = User.query.filter_by(username=username).first()
    item_id = request.form['id']
    item_name = request.form['name']
    item_price = request.form['price']
    carrinho = Carrinho(user_id=user.id, product_id=item_id, product_name=item_name, product_price=item_price)
    #item = Carrinho.query.get([item_id, item_name, item_price])
    db.session.add(carrinho)
    db.session.commit()
    return redirect('/cart')

@app.route("/cart")
def cart():
    if 'user' in session:
        # Só precisa do username para fazer o Login
        username = session['user']
        # Query the database to get the user's profile information
        user = User.query.filter_by(username=username).first()
        # Query the database to get the user's carrinho information
        products = Carrinho.query.filter_by(user_id=user.id).all()

        return render_template('cart.html', user=user, products=products)
    else:
        return render_template('login-register.html')

@app.route('/delete', methods=['POST'])
def delete_item():
    item_id = request.form['id']
    item = Carrinho.query.get(item_id)
    db.session.delete(item)
    db.session.commit()
    return redirect('/cart')

@app.route("/404")
def error_404():
    return render_template("404.html")
    
@app.route("/checkout")
def checkout():
    return render_template("checkout.html")

@app.route("/profile")
def profile():
    if 'user' in session:
        # Só precisa do username para fazer o Login
        username = session['user']
        # Query the database to get the user's profile information
        user = User.query.filter_by(username=username).first()
        # Query the database to get the user's carrinho information
        #products = Carrinho.query.filter_by(username=username).first()
        #products = Carrinho.query.filter_by(user_id=user.id).all()

        #products = Carrinho.query.filter_by(user_id=user.id).all()

        return render_template('profile.html', user=user)
    else:
        return render_template('login-register.html')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.route("/profileupdate", methods=['POST'])
def carrinho_send():
    username = session['user']
    user = User.query.filter_by(username=username).first()

    carrinho = Carrinho(user_id=user.id, product_id=1, product_name="teste", product_price=1)

    #Indica o que vai fazer
    db.session.add(carrinho)
    #Faz o Envio
    db.session.commit()
    return redirect(url_for('cart'))

@app.route('/logout')
def logout():
    # Remove the user from the session
    session.pop('user', None)
    return redirect(url_for('profile'))

@app.route("/shop")
def shop():
    return render_template("shop.html")

@app.route("/shop-single")
def shop_single():
    return render_template("shop-single.html")
    

@app.route("/login-form", methods=['POST'])
def login_form():
    # Get the username and password from the form
    username = request.form['login-form-username']
    password = request.form['login-form-password']

    # Check if the username and password are correct
    user_form = User.query.filter_by(username=username, password=password).first()
    if user_form:
        # Create a session
            session['user'] = user_form.username
            return redirect(url_for('index'))
    else:
        # Login failed
        return redirect(url_for('error_404'))
    

@app.route("/register-form", methods=['POST'])
def register_form():
    # Get the username and password from the form
    username = request.form['register-form-username']
    password = request.form['register-form-password']
    email = request.form['register-form-email']
    first_name = request.form['register-form-firstname']
    last_name = request.form['register-form-lastname']
    phone = request.form['register-form-phone']

    role = Role(role="Cliente")
    register = User(username=username, password=password, email=email, firstname=first_name,lastname=last_name, phone=phone, role=role)
    morada = Morada(city="Aveiro", postal_code="3800-000", user=register)

    #Indica o que vai fazer 
    db.session.add_all([register, role, morada])
    #Faz o Envio
    db.session.commit()
    
    if register:
        session['user'] = register.username
        return redirect(url_for('profile'))
    else:
        # Login failed
        return redirect(url_for('error_404'))

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)



