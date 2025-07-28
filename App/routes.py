from flask import render_template, redirect, url_for, flash, request
from .model import Item, User
from App import app, db
from .forms import RegisterForm, LoginForm
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, login_user, logout_user, login_required, current_user


login_manager = LoginManager(app)
login_manager.login_view = 'login_page'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/')
def home_page():
    return render_template('index.html')

@app.route('/market')
@login_required
def market_page():
    items = Item.query.filter_by(user_id=None).all()
    purchased_items = Item.query.filter_by(user_id=current_user.id).all()
    return render_template('market.html', items=items, purchased_items=purchased_items)

@app.route('/register', methods=['GET', 'POST'])
def register_page():
    form = RegisterForm()
    if form.validate_on_submit():
        hashed_password = generate_password_hash(form.password1.data)
        new_user = User(
            username=form.username.data,
            email=form.email.data,
            password_hash=hashed_password
        )
        db.session.add(new_user)
        db.session.commit()
        login_user(new_user)  # Automatically log in the user after registration
        flash('Account created successfully! You are now logged in.', 'success')
        return redirect(url_for('market_page'))
    elif form.is_submitted() and not form.validate():
        for field, errors in form.errors.items():
            for error in errors:
                flash(f"{field.capitalize()}: {error}", 'danger')
    return render_template('register.html', form=form)

# route for the login page
@app.route('/login', methods=['GET', 'POST'])
def login_page():
    form = LoginForm()
    error = None
    if form.validate_on_submit():
        user = User.query.filter(
            (User.email == form.email_or_username.data) | 
            (User.username == form.email_or_username.data)
        ).first()
        if user and check_password_hash(user.password_hash, form.password.data):
            login_user(user)  # Add this line
            flash('Logged in successfully!', 'success')
            return redirect(url_for('market_page'))
        else:
            error = 'Invalid email/username or password. Please try again.'
    return render_template('login.html', form=form, error=error)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out.', 'info')
    return redirect(url_for('home_page'))

@app.route('/purchase/<int:item_id>', methods=['GET', 'POST'])
@login_required
def purchase_item(item_id):
    item = Item.query.get_or_404(item_id)
    if item.user_id:
        flash('This item has already been purchased.', 'danger')
        return redirect(url_for('market_page'))
    if current_user.points >= item.price:
        current_user.points -= item.price
        item.user_id = current_user.id
        db.session.commit()
        flash(f'You have successfully purchased {item.item_name}!', 'success')
    else:
        flash('You do not have enough points to purchase this item.', 'danger')
    return redirect(url_for('market_page'))

@app.route('/sell/<int:item_id>', methods=['GET', 'POST'])
@login_required
def sell_item(item_id):
    item = Item.query.get_or_404(item_id)
    if item.user_id != current_user.id:
        flash('You can only sell items that you own.', 'danger')
        return redirect(url_for('market_page'))
    current_user.points += item.price
    item.user_id = None
    db.session.commit()
    flash(f'You have successfully sold {item.item_name}!', 'success')
    return redirect(url_for('market_page'))