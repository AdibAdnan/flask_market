from App import app, db
from App.model import Item

with app.app_context():
    db.drop_all()
    db.create_all()
    print("All tables dropped and recreated.")
    
    items = [
        Item(item_name="Item 1", barcode="123456789001", price=10),
        Item(item_name="Item 2", barcode="123456789002", price=20),
        Item(item_name="Item 3", barcode="123456789003", price=30),
        Item(item_name="Item 4", barcode="123456789004", price=40),
        Item(item_name="Item 5", barcode="123456789005", price=50),
    ]
    db.session.add_all(items)
    db.session.commit()
    print("5 items added to the Item table.")
