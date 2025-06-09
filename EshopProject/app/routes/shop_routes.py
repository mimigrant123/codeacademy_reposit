from flask import Blueprint, render_template, redirect, url_for, flash, request, jsonify
from flask_login import current_user, login_required
from ..extensions import db
from ..models import Product, CartItem, Order, OrderItem

shop_bp = Blueprint('shop', __name__, template_folder='../templates')

@shop_bp.route('/')
def index():
    products = Product.query.limit(10).all()
    return render_template('index.html', products=products)


@shop_bp.route('/add_to_cart/<int:product_id>')
@login_required
def add_to_cart(product_id):
    product = Product.query.get_or_404(product_id)
    existing = CartItem.query.filter_by(user_id=current_user.id, product_id=product_id).first()
    if existing:
        existing.quantity += 1
    else:
        new_item = CartItem(user_id=current_user.id, product_id=product_id, quantity=1)
        db.session.add(new_item)
    db.session.commit()
    flash(f'Added {product.name} to cart.', 'success')
    return redirect(url_for('shop.cart'))


@shop_bp.route('/cart')
@login_required
def cart():
    items = CartItem.query.filter_by(user_id=current_user.id).all()
    total = sum(item.product.price * item.quantity for item in items)
    return render_template('cart.html', items=items, total=total)


@shop_bp.route('/remove_from_cart/<int:item_id>')
@login_required
def remove_from_cart(item_id):
    item = CartItem.query.get_or_404(item_id)
    if item.user_id != current_user.id:
        flash('Unauthorized action.', 'danger')
        return redirect(url_for('shop.cart'))
    db.session.delete(item)
    db.session.commit()
    flash('Item removed from cart.', 'info')
    return redirect(url_for('shop.cart'))


@shop_bp.route('/checkout', methods=['POST'])
@login_required
def checkout():
    items = CartItem.query.filter_by(user_id=current_user.id).all()
    if not items:
        flash('Your cart is empty.', 'warning')
        return redirect(url_for('shop.cart'))

    total = sum(item.product.price * item.quantity for item in items)
    order = Order(user_id=current_user.id, total_amount=total, status='created')
    db.session.add(order)
    db.session.flush()  # get order.id without committing

    for item in items:
        oi = OrderItem(
            order_id=order.id,
            product_id=item.product_id,
            quantity=item.quantity,
            unit_price=item.product.price
        )
        db.session.add(oi)
        db.session.delete(item)
    db.session.commit()

    return redirect(url_for('shop.payment', order_id=order.id))

@shop_bp.route('/product/<int:product_id>')
def view_product(product_id):
    product = Product.query.get_or_404(product_id)
    return render_template('product.html', product=product)


@shop_bp.route('/payment/<int:order_id>')
@login_required
def payment(order_id):
    order = Order.query.get_or_404(order_id)
    if order.user_id != current_user.id:
        flash('Unauthorized access to payment.', 'danger')
        return redirect(url_for('shop.index'))
    return render_template('payment.html', order=order)


@shop_bp.route('/payment_complete/<int:order_id>', methods=['POST'])
@login_required
def payment_complete(order_id):
    order = Order.query.get_or_404(order_id)
    if order.user_id != current_user.id:
        return jsonify({'error': 'Unauthorized'}), 403

    data = request.get_json()
    result = data.get('result')
    if result == 'success':
        order.status = 'pending'
    else:
        order.status = 'declined'
    db.session.commit()
    return jsonify({'status': order.status})
