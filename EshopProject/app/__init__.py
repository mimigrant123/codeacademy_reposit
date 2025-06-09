import os
from flask import Flask
from .extensions import db, login_manager
from .models import Product, ProductImage

def create_app():
    app = Flask(
        __name__,
        static_folder=os.path.join("static"),
        template_folder=os.path.join("templates")
    )

    app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'secure-key')
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///eshop.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'

    # Register Blueprints
    from .routes.auth_routes import auth_bp
    from .routes.shop_routes import shop_bp
    from .routes.admin_routes import admin_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(shop_bp)
    app.register_blueprint(admin_bp)

    return app


def create_tables_and_seed(app):
    """
    Creates tables and seeds Products + ProductImages by grouping all files
    in app/static/images/ whose filename starts with the same 'Basket_##' prefix.
    """
    with app.app_context():
        # 1) Create tables (if they don't yet exist)
        db.create_all()

        # 2) If products already exist, skip seeding
        if Product.query.count() > 0:
            return

        # 3) Point to the folder where your images live
        images_dir = os.path.join(app.root_path, 'static', 'images')
        if not os.path.isdir(images_dir):
            return

        # 4) List all .jpg/.jpeg/.png files
        image_files = sorted(
            f for f in os.listdir(images_dir)
            if f.lower().endswith(('.jpg', '.jpeg', '.png'))
        )
        if not image_files:
            return

        # 5) Group them by the "Basket_XX" prefix:
        #    - Strip off the extension → "Basket_09_2.jpg" → "Basket_09_2"
        #    - Split on '_' and take first two segments → ["Basket","09","2"] → "Basket_09"
        grouped = {}
        for fname in image_files:
            name_no_ext = fname.rsplit('.', 1)[0]     # "Basket_09_2.jpg" → "Basket_09_2"
            parts = name_no_ext.split('_')
            if len(parts) >= 2:
                # Combine the first two parts to form the group key
                group_base = f"{parts[0]}_{parts[1]}"  # e.g. "Basket_09"
            else:
                # (In practice, everything is "Basket_##", but just in case:)
                group_base = name_no_ext               # e.g. "Basket" if no underscore found

            grouped.setdefault(group_base, []).append(fname)

        # 6) Now create one Product per group key, and multiple ProductImage rows
        for group_key, file_list in sorted(grouped.items(), key=lambda x: x[0]):
            # Derive a nice display name and price. If group_key="Basket_09", then:
            try:
                _, number = group_key.split('_')
                product_name  = f"Basket {int(number)}"
                product_price = 20.0 * int(number)
            except ValueError:
                # Fallback if group_key isn't "Basket_##" exactly
                product_name  = group_key.replace('_', ' ')
                product_price = 20.0

            product = Product(
                name=product_name,
                description=f"A beautiful basket: {product_name}",
                price=product_price
            )
            db.session.add(product)
            db.session.flush()  # so product.id is set before creating images

            # Create one ProductImage per filename in this group
            for fname in file_list:
                img = ProductImage(
                    product_id=product.id,
                    filename=fname
                )
                db.session.add(img)

        # 7) Commit everything
        db.session.commit()