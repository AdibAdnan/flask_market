from App import app, db
import App.model  # Ensure models are imported

with app.app_context():
    db.create_all()
    print("Database and tables created.")
