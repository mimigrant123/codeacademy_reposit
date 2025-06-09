from app import create_app, create_tables_and_seed
from app.extensions import db
from app.models import User

app = create_app()

email = 'admin@admin.com'
username = 'admin'
password = 'admin123'

# Ensure tables exist and products are seeded
create_tables_and_seed(app)

with app.app_context():
    # Looking for user with same email
    u = User.query.filter_by(email=email).first()

    if u is None:
        # If not found, create a new user
        u = User(username=username, email=email)
        u.set_password(password) 
        u.is_admin = True
        db.session.add(u)
        db.session.commit()
        print(f"Created new admin user: {email}")
    else:
        # If found, just mark them as admin
        if not u.is_admin:
            u.is_admin = True
            db.session.commit()
            print(f"Existing user {email} is now admin.")
        else:
            print(f"User {email} is already an admin.")
