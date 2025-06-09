from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import current_user, login_required
from ..extensions import db
from ..models import Order, OrderItem, Product, User

admin_bp = Blueprint('admin', __name__, url_prefix='/admin', template_folder='../templates')

ALLOWED_ORDER_STATUSES = ['created', 'pending', 'delivered', 'declined']


@admin_bp.route('/')
@login_required
def admin_dashboard():
    # Only admins can view this
    if not current_user.is_admin:
        flash('Admin access required.', 'danger')
        return redirect(url_for('shop.index'))

    # Fetch all orders, newest first
    orders = Order.query.order_by(Order.created_at.desc()).all()
    return render_template('admin.html', orders=orders)


@admin_bp.route('/update_status/<int:order_id>', methods=['POST'])
@login_required
def update_status(order_id):
    # Only admins can update
    if not current_user.is_admin:
        flash('Admin access required.', 'danger')
        return redirect(url_for('shop.index'))

    new_status = request.form.get('status')
    if new_status not in ALLOWED_ORDER_STATUSES:
        flash('Invalid status selected.', 'warning')
        return redirect(url_for('admin.admin_dashboard'))

    order = Order.query.get_or_404(order_id)
    order.status = new_status
    db.session.commit()
    flash(f"Order #{order.id} status updated to '{new_status}'.", 'success')
    return redirect(url_for('admin.admin_dashboard'))


@admin_bp.route('/order/<int:order_id>')
@login_required
def view_order(order_id):
    # Only admins can view any order
    if not current_user.is_admin:
        flash('Admin access required.', 'danger')
        return redirect(url_for('shop.index'))

    order = Order.query.get_or_404(order_id)
    # Fetch all OrderItem rows for this order (products, quantities, unit prices)
    items = OrderItem.query.filter_by(order_id=order.id).all()
    return render_template('order_details.html', order=order, items=items)
